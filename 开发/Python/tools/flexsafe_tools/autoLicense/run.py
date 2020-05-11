# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven-office‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: FlexSafe.py
@time: 2019/4/26 16:54
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import json
import time
import pymysql
from loguru import logger

import requests
from autoLicense import utils
from flexsafe_utils.SSHConnection import SSHConnection
from flexsafe_utils.common import ssh_login, check_jetty, parse_ip

current_dir = os.path.dirname(os.path.abspath(__file__))
license_path = os.path.join(current_dir, 'license')
licenseLib_path = os.path.join(current_dir, 'libLicenseConfig.so')


class FlexSafe:
    def __init__(self):
        self.input_ip = input("请输入Flexsafe Server IP：172.16.")
        self.base_url = ' http://' + parse_ip(self.input_ip)
        self.apply_timestamp = None
        self.keygen = None
        self.files = None

    # 通过downloadUUIDFile接口下载keyGen
    def get_keygen_text(self):
        url = self.base_url + '/api/v1/license/downloadUUIDFile'
        try:
            r = requests.get(url=url, timeout=5)
        except:
            logger.error("请求:【%s】失败，请检查IP输入是否正确和FlexSafe服务器是否可正常访问！" % self.base_url)
            sys.exit(1)
        if r.status_code != 200:
            logger.error("请求:【%s】失败，请检查IP输入是否正确和FlexSafe服务器是否可正常访问！" % self.base_url)
            sys.exit(1)
        self.keygen = r.text
        logger.info('-----从【%s】获取keyGen成功-----' % self.base_url)
        logger.debug('KeyGen:' + self.keygen)
        self.files = {'file': ('KeyReg', self.keygen, 'multipart/form-data',)}

    # 通过keygen内容查找license服务器中MySQL的记录，并删除该条记录
    def clear_license(self):
        ssh_host = "172.16.71.180"  # 堡垒机ip地址或主机名
        ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
        ssh_user = "cfservice"  # 这是你在堡垒机上的用户名
        ssh_password = "cfzoom2016"  # 这是你在堡垒机上的用户密码
        mysql_host = "localhost"  # 这是你mysql服务器的主机名或ip地址
        mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
        mysql_user = "root"  # 这是你mysql数据库上的用户名
        mysql_password = "cloudfort"  # 这是你mysql数据库的密码
        mysql_db = "licenseserver"  # mysql服务器上的数据库名

        # with SSHTunnelForwarder(
        #         (ssh_host, ssh_port),
        #         ssh_username=ssh_user,
        #         ssh_password=ssh_password,
        #         remote_bind_address=(mysql_host, mysql_port)) as server:
        conn = pymysql.connect(host=mysql_host,
                               port=mysql_port,
                               user=mysql_user,
                               passwd=mysql_password,
                               db=mysql_db)

        cursor = conn.cursor()
        cursor.execute('''DELETE FROM license_info WHERE uuid='%s';''' % self.keygen)
        conn.commit()
        cursor.close()
        conn.close()

    # 模拟登陆license服务器，请求发送license至对应邮箱
    def applyLicense(self):
        logger.warning('如需更改license相关配置，请编辑文件【%s】' % os.path.join(current_dir, 'conf.cfg'))

        # 登陆，获取session
        base_url = utils.get_conf_value('license', 'host')
        userName = utils.get_conf_value('license', 'userName')
        passwd = utils.get_conf_value('license', 'passwd')
        session = requests.Session()
        post_json = {
            "email": userName,
            "password": passwd,
            "role": "ADMIN"
        }
        r = session.post(url=base_url + '/api/v1/login', json=post_json)
        logger.debug('try login license server---->' + r.text)
        if 'role' in json.loads(r.text):
            logger.info('-----登陆License Server成功-----')
            logger.debug('Response:' + r.text)
        else:
            logger.error('Login license server fail!')
            logger.debug('Response:' + r.text)
            sys.exit(1)
        post_data = {
            'userId': '32',
            'version': 'V1.1',
            'type': 'ALL',
            'validDays': utils.get_conf_value('license', 'validDays'),
        }

        apply_r = session.post(url=base_url + '/api/v1/license', files=self.files, data=post_data)
        logger.debug('apply license info:' + apply_r.text)
        logger.info("-----license发送至邮箱...-----")
        self.apply_timestamp = time.time()

    # 模拟登陆邮箱，并下载license
    def downloadLicenseFromMail(self):
        for i in range(7):
            logger.info('-----正在第%s次尝试从邮件中获取license...-----' % (i + 1))
            latest_mail = utils.get_latest_mail()
            mail_date = latest_mail['date']
            subject = latest_mail.get('headers').get('Subject')
            mail_time_stamp = time.mktime(mail_date.timetuple())
            if subject == 'Flexsafe License' and (mail_time_stamp - self.apply_timestamp > 0):
                with open(license_path, 'wb') as f:
                    f.write(latest_mail.get('attachments')[0][1])
                    logger.info('-----从邮件【%s】获取license成功-----' % utils.get_conf_value('license', 'mail_name'))
                    return
            time.sleep(2)
        logger.error("邮件未收到license，请手动登陆邮箱检查")

    # 获取libLicenseConfig.so
    def getLibLicense(self):
        base_url = utils.get_conf_value('libLicense', 'host')
        company = utils.get_conf_value('libLicense', 'company')
        maxUserNumber = utils.get_conf_value('libLicense', 'maxUserNumber')
        maxCapacity = utils.get_conf_value('libLicense', 'maxCapacity')
        canLock = utils.get_conf_value('libLicense', 'canLock')

        session = requests.Session()
        post_data = {
            'company': company,
            'maxUserNumber': maxUserNumber,
            'maxCapacity': maxCapacity,
            'canLock': canLock,
        }
        # 向LibLicenseServer上传keygen
        uoload_keygen = session.post(url=base_url + '/api/userConfig/uploadConfig', files=self.files, data=post_data, )
        logger.info("-----正在向libLicenseServer上传keygen...-----")
        logger.debug('uoload_keygen:' + uoload_keygen.text)

        # 从LibLicenseServer下载license
        params = {
            'company': company
        }
        downlibLicenseFile = session.get(base_url + '/api/userConfig/downloadFile', params=params)
        with open(licenseLib_path, 'wb') as f:
            if downlibLicenseFile.status_code == 200:
                f.write(downlibLicenseFile.content)
                logger.info('-----下载 【libLicenseConfig.so】文件成功!-----')
            else:
                logger.error('下载 【libLicenseConfig.so】文件失败!')

    # 移动license、libLicenseConfig.so至/usr/lib/jni/
    def mvFiles(self, ssh_name, ssh_passwd, confirm):
        localpath = [license_path, licenseLib_path]
        remotepath = '/home/%s/' % ssh_name
        if ssh_name == 'root':
            remotepath = '/root/'
        try:
            ssh = SSHConnection(parse_ip(self.input_ip), 22, ssh_name, ssh_passwd)
        except:
            logger.error('未知错误')
            logger.info('ssh_name:' + ssh_name)
            logger.info('ssh_passwd:' + ssh_passwd)
            logger.info('host:' +parse_ip(self.input_ip))
            sys.exit(1)
        for i in localpath:
            logger.info("-----正在上传【%s】至Flexsafe....-----" % i)
            logger.debug('remotepath:' + remotepath + str(i).split('/')[-1])
            ssh.put(i, remotepath + str(i).split('/')[-1])
        ssh.exec_command('cd /home/%s/;sudo mv license libLicenseConfig.so /usr/lib/jni/' % ssh_name, ssh_passwd)

        if confirm == '0' or confirm == '':
            if ssh_name != 'root':
                ls = 'sudo ls /etc/init.d/ | grep jetty'
                jetty_v = ssh.exec_command(ls, ssh_passwd).decode('utf-8').split('\r\n')[2]
                logger.info("-----正在重启Jetty....-----")
                logger.debug('jetty_v:' + jetty_v)
                ssh.exec_command('sudo service %s restart' % jetty_v, ssh_passwd)
            else:
                try:
                    ssh.exec_command('service jettydr restart', ssh_passwd)
                    ssh.exec_command('service jettyd restart', ssh_passwd)
                except:
                    logger.error('重启Jetty失败，请手动重启！')
                    os._exit(0)
        if confirm == '1':
            ssh.exec_command('sudo reboot', ssh_passwd)

        # 检查Jetty状态
        http_url = 'http://' + parse_ip(self.input_ip)
        if ':' not in self.input_ip:
            http_url = 'http://' + parse_ip(self.input_ip) + ':8080'
        check_jetty(http_url, 200)


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    print('''
    执行步骤：

        1.使用默认的SSH账号【cfservice】和密码【cfzoom2016】尝试连接FlexServer，若失败，提示用户进行输入；
        2.下载FlexServer的KeyGen文件；
        3.通过KeyGen查找License Server上MySQL的license记录，若存在，则进行删除；
        4.读取License配置文件【conf.cfg】，请求License Server将license文件发送至邮箱【761701732@qq.com】；
        5.读取LibLicense配置文件【conf.cfg】，请求并获取到【libLicenseConfig.so】文件;
        6.模拟登陆邮箱【761701732@qq.com】，或取到附件【license】；
        7.SSH登陆FlexServer，将license、libLicenseConfig.so移动至路径【/usr/lib/jni】；
        8.提供后续操作选项：重启Jetty、重启服务器；


    ''')
    f = FlexSafe()
    confirm = input('''请输入操作选项（默认为0）：
    0---->重启Jetty;
    1---->重启服务器;
    ''')
    ssh_account = ssh_login(parse_ip(f.input_ip))
    f.get_keygen_text()
    f.getLibLicense()
    f.clear_license()
    f.applyLicense()
    f.downloadLicenseFromMail()
    f.mvFiles(ssh_account[0], ssh_account[1], confirm)
