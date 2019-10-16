# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: common.py
@time: 2019/5/13 15:08
"""
import os
import re
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import base64
import json
import time
import pymysql
import os
import sys

from flexsafe_utils.SSHConnection import SSHConnection

from flexsafe_utils.Encrypy import PrpCrypt
import requests

cp = PrpCrypt()
default_admin_name = 'admin123'
default_admin_passwd = '123qwe'
default_ssh_name = 'cfservice'
default_ssh_passwd = 'cfzoom2016'
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

header = {
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": "",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
from colorama import Fore
from prettytable import PrettyTable


class Colored(object):
    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    def white(self, s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

    def blue(self, s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET


def check_authorizatin(host, admin_name, admin_passwd):
    if not is_new_version(host):
        header.update(
            {'Authorization': 'Basic ' + bytes.decode(base64.b64encode(str.encode(admin_name + ':' + admin_passwd)))})
    else:
        header.update({'Authorization': cp.create_Authorization(admin_name, admin_passwd)})

    url = 'http://%s/api/v1/authentication' % host
    try:
        r = requests.get(url=url, headers=header, timeout=5)
        if r.status_code == 200:
            logger.info('管理员认证成功')
            return True
        else:
            logger.error('管理员认证失败，请检查账号和密码')
            logger.debug(r.text)
            return False
    except:
        logger.error('登陆FlexSafe失败，请检查地址或服务是否正常！管理员是否已经注册？')


def check_ssh_authorization(host, ssh_name, ssh_passwd):
    try:
        if ':' in host:
            host = host.split(':')[0]
        logger.debug('ssh_host:%s' % host)
        SSHConnection(host, 22, ssh_name, ssh_passwd)
        return True
    except:
        logger.error('【SSH】登陆FlexSafe Server失败，请检查【SSH】用户账号、密码、IP是否正确！')
        return False


def clear_file_content(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.truncate()


# 获取flexsafe认证
def flexsafe_login(host):
    is_new = is_new_version(host)
    logger.info("尝试使用默的管理员账号【admin123】和密码【123qwe】登录......")
    auth_result = check_authorizatin(host, default_admin_name, default_admin_passwd)
    if auth_result == None:
        sys.exit(1)
    if not auth_result:
        logger.error("使用默的管理员账号【admin123】和密码【123qwe】登录失败，请手动登录！")
        for i in range(3):
            admin_name = input('请输入FlexSafe Server 管理员账号：')
            admin_pwd = input('请输入FlexSafe Server 管理员密码：')
            if check_authorizatin(host, admin_name, admin_pwd):
                if not is_new:
                    authorization = 'Basic ' + bytes.decode(base64.b64encode(str.encode(admin_name + ':' + admin_pwd)))
                    return authorization, admin_name, admin_pwd
                authorization = cp.create_Authorization(admin_name, admin_pwd)
                return authorization, admin_name, admin_pwd
        logger.error("三次都不对，下面的时间留给你，去怀疑人生吧。。。")
        sys.exit()

    if not is_new:
        authorization = 'Basic ' + bytes.decode(
            base64.b64encode(str.encode(default_admin_name + ':' + default_admin_passwd)))
        return authorization, default_admin_name, default_admin_passwd
    authorization = cp.create_Authorization(default_admin_name, default_admin_passwd)
    return authorization, default_admin_name, default_admin_passwd


# 获取ssh认证
def ssh_login(host):
    logger.info("尝试使用默的SSH账号【cfservice】和密码【cfzoom2016】登录......")
    ssh_auth_result = check_ssh_authorization(host, default_ssh_name, default_ssh_passwd)
    logger.debug('ssh_name:%s' % default_ssh_name)
    logger.debug('ssh_pwd:%s' % default_ssh_passwd)
    if ssh_auth_result == None:
        sys.exit(1)
    if not ssh_auth_result:
        logger.error("使用默的SSH账号【cfservice】和密码【cfzoom2016】登录失败，请手动登录！")
        for i in range(3):
            ssh_name = input('请输入FlexSafe Server 【SSH】账号：')
            ssh_pwd = input('请输入FlexSafe Server 【SSH】账号密码：')
            logger.debug('ssh_name:%s' % ssh_name)
            logger.debug('ssh_pwd:%s' % ssh_pwd)
            if check_ssh_authorization(host, ssh_name, ssh_pwd):
                logger.info("SSH可以成功连接")
                return ssh_name, ssh_pwd
    return default_ssh_name, default_ssh_passwd


# 获取FlexSafe版本
def get_flexsafe_version(host):
    base_url = 'http://%s/api/v1/status' % host
    logger.debug('base_url:%s' % base_url)
    try:
        r = requests.get(base_url, timeout=5)
        logger.debug(r.text)
        version = json.loads(r.text)['data']['flexsafeVersion']
        return version
    except:
        logger.error("获取FlexSafe版本失败，请检查地址或FlexSafe服务是否正常！，若使用非8080端口，请加上该端口号")
        sys.exit(1)


# 配置邮件服务器
def config_mail(host, authorization):
    logger.info('正在设置邮箱服务器...')
    header.update({"Authorization": authorization})
    base_url = 'http://%s/api/v1/emailConfig' % host
    global put_data
    s0 = {
        "smtpHost": "smtp.qq.com",
        "smtpPort": 587,
        "username": "minxi.sun@qq.com",
        "password": "sscdgnpefbtvdhhj"
    }
    s1 = {
        "smtpHost": "imap.exmail.qq.com",
        "smtpPort": 25,
        "username": "miaoniandu@cloudfort.ml",
        "password": "Aaa00123"
    }
    s2 = {
        "smtpHost": "imap.exmail.qq.com",
        "smtpPort": 25,
        "username": "xuetong.yang@cloudfortdata.com",
        "password": "Aaa00123"
    }
    s3 = {
        "smtpHost": "220.181.12.13",
        "smtpPort": 25,
        "username": "cloudfortdata01@163.com",
        "password": "2wsx3edc"
    }
    s4 = {
        "smtpHost": "imap.exmail.qq.com",
        "smtpPort": 25,
        "username": "tianchi.sun@cloudfortdata.com",
        "password": "Sun178"
    }
    s5 = {
        "smtpHost": "220.181.15.113",
        "smtpPort": 25,
        "username": "stc178@126.com",
        "password": "123qwe"
    }
    s6 = {
        "smtpHost": "imap.exmail.qq.com",
        "smtpPort": 25,
        "username": "qian.wang@cloudfortdata.com",
        "password": "WANGqian0510"
    }

    c = Colored()
    pt = PrettyTable()
    pt.field_names = ['序号', '邮箱']
    pt.add_row([c.blue('0'), c.magenta(s0['username'])])
    pt.add_row([c.blue('1'), c.magenta(s1['username'])])
    pt.add_row([c.blue('2'), c.magenta(s2['username'])])
    pt.add_row([c.blue('3'), c.magenta(s3['username'])])
    pt.add_row([c.blue('4'), c.magenta(s4['username'])])
    pt.add_row([c.blue('5'), c.magenta(s5['username'])])
    pt.add_row([c.blue('6'), c.magenta(s6['username'])])
    pt.align['序号'] = "l"
    pt.align['邮箱'] = "l"
    pt.horizontal_char = c.cyan('-')
    pt.vertical_char = c.cyan('|')
    pt.junction_char = c.cyan('+')
    print(pt)

    choice = input('请输入对应邮箱的序号，默认设置【%s】：' % s1['username'])
    if choice == '0':
        put_data = s0
    elif choice == '1':
        put_data = s1
    elif choice == '2':
        put_data = s2
    elif choice == '3':
        put_data = s3
    elif choice == '4':
        put_data = s4
    elif choice == '5':
        put_data = s5
    elif choice == '6':
        put_data = s6
    elif choice == '':
        put_data = s1
    else:
        logger.error('该选项不存在！')
        sys.exit(1)

    try:
        r = requests.put(url=base_url, headers=header, json=put_data, timeout=8)
        if (r.status_code != 200):
            logger.error("设置邮箱服务器【%s】失败" % put_data['username'])
            logger.info('设置邮箱服务器响应：' + r.text)
        else:
            logger.info("设置邮箱服务器【%s】成功" % put_data['username'])
    except requests.exceptions.ReadTimeout:
        logger.error("设置邮件服务器超时，请手动设置！")


# 开启加锁
def enable_clock(host, authorization):
    logger.info('正在开启加锁功能...')
    header.update({"Authorization": authorization})
    base_url = 'http://{}/api/v1/globalConfig/%5B%7B%22name%22:%22global.system.file.lock.status%22,%22value%22:%221%22%7D%5D'.format(
        host)
    put_data = {}

    r = requests.put(url=base_url, headers=header, json=put_data)
    if (r.status_code != 200):
        logger.error("开启加锁失败")
        logger.info('开启加锁服务器响应：' + r.text)
    else:
        logger.info("开启加锁成功！")


# 开启传用管控
def enable_special_control(host, authorization):
    logger.info('正在开启专用管控功能...')
    header.update({"Authorization": authorization})
    base_url = 'http://{}/api/v1/globalConfig/%5B%7B%22name%22:%22global.web.special.control%22,%22value%22:%221%22%7D%5D'.format(
        host)
    put_data = {}

    r = requests.put(url=base_url, headers=header, json=put_data)
    if (r.status_code != 200):
        logger.error("开启加锁失败")
        logger.debug('开启加锁服务器响应：' + r.text)
    else:
        logger.info("开启专用管控功能成功！")


# 是否是新版本（authrization不一样）
def is_new_version(host):
    if get_flexsafe_version(host)[:5] <= '1.9.3.0':
        return False
    return True


# 切分list
def split_list(m_list, num):
    logger.info('正在开启线程...')
    return [m_list[i:i + num] for i in range(0, len(m_list), num)]


def excuseSQL(host, ssh_account, databse, sql):
    # 获取所有项目组ID
    ssh_host = host  # 堡垒机ip地址或主机名
    ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
    ssh_user = ssh_account[0]  # 这是你在堡垒机上的用户名
    ssh_password = ssh_account[1]  # 这是你在堡垒机上的用户密码
    mysql_host = "localhost"  # 这是你mysql服务器的主机名或ip地址
    mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
    mysql_user = "root"  # 这是你mysql数据库上的用户名
    mysql_password = "cloudfort"  # 这是你mysql数据库的密码
    mysql_db = databse  # mysql服务器上的数据库名

    from sshtunnel import SSHTunnelForwarder
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(mysql_host, mysql_port)) as server:
        conn = pymysql.connect(host=mysql_host,
                               port=server.local_bind_port,
                               user=mysql_user,
                               passwd=mysql_password,
                               db=mysql_db)

        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        id_list = [x[0] for x in results]
        cursor.close()
        conn.close()
        logger.info('查询到所有组ID：%s' % str(id_list))
        return id_list


def upload_file(host, authorization, remote_path, file_name):
    upload_url = 'http://%s/api/v1/filelists/uploadFile' % host
    header = {
        "Authorization": authorization,
    }
    post_data = {
        'userId': '1',
        'remotePath': remote_path,
        'isOverWrite': '-1',
        'isSendEmail': 'false',
        'flowChunkNumber': '1',
        'flowChunkSize': '20971520',
        'flowCurrentChunkSize': '4',
        'flowTotalSize': '4',
        'flowIdentifier': '4-1txt',
        'flowFilename': file_name,
        'flowRelativePath': file_name,
        'flowTotalChunks': '1',
    }
    files = {'file': (file_name, '1111', 'text/plain')}
    r = requests.post(url=upload_url, files=files, headers=header, data=post_data, timeout=300, verify=False)
    if r.status_code == 200:
        logger.info('文件上传成功')
    else:
        logger.error('文件上传失败')
        logger.debug(r.text)


# 添加云备份服务器
def add_cloud_backup(host, authorization, type):
    header.update({"Authorization": authorization})
    base_url = 'http://{}/api/v1/backup/config/add?itemId='.format(
        host)
    post_data = {}
    if type == 'ace':
        logger.info('正在添加阿里云备份服务器...')
        post_data.update({
            "name": "aliyun_backup_%s" % str(int(time.time() * 1000))[9:],
            "backupServerType": "1",
            "serverIp": "oss-cn-shanghai.aliyuncs.com",
            "accessId": "LTAIdDa0FSnWHAO9",
            "accessKey": "yNqeNPxypxsV7zBaZt4gAaZNRIxxDM",
            "bucketName": str(int(time.time() * 1000))
        })

    if type == 'aws':
        logger.info('正在添加亚马逊备份服务器...')
        post_data.update({
            "name": "aws_backup_%s" % str(int(time.time() * 1000))[9:],
            "backupServerType": "2",
            "serverIp": "s3://s3.cn-north-1.amazonaws.com.cn",
            "accessId": "AKIAPYYWDIHERMC6R6QA",
            "accessKey": "Y93gi6y2AtKYBzneebwiT0YYck62CCS4/bgZ0ZD7",
            "bucketName": str(int(time.time() * 1000))
        })

    r = requests.post(url=base_url, headers=header, json=post_data)
    logger.debug('添加云备份服务器响应：' + r.text)
    if (r.status_code != 200):
        logger.error("添加云备份服务器失败,请手动添加~")
        logger.error('Response:' + r.text)
    else:
        if 'aliyun_backup' in r.text:
            logger.info("添加【阿里云】备份服务器成功！")
        elif 'aws_backup' in r.text:
            logger.info("添加【亚马逊】备份服务器成功！")
        else:
            logger.info("不知名备份服务器添加成功")


# 获取系统当前时间
def get_current_time():
    return str(os.popen('date').read()).strip()


# 获取系统当前时间
def check_jetty(http_url, times):
    for i in range(1, times):
        logger.info('Jetty重启中，正在第%s次连接服务器，请稍后...' % i)
        time.sleep(1)
        try:
            r = requests.get(url=http_url)
            if r.status_code == 200:
                time.sleep(2)
                try:
                    r1 = requests.get(url=http_url, verify=False)
                    if r1.status_code == 200:
                        logger.warning('Jetty运行中....')
                        logger.warning('访问地址：' + http_url)
                        return
                except:
                    logger.error('Jetty重启失败，请手动配置！')
                    break
        except:
            pass
    logger.error('Jetty重启失败，请手动配置！')
    os._exit(1)


def parse_ip(input_ip):
    ip_lenth = len(re.findall(r'\d\.\d', input_ip))
    if ip_lenth == 1:
        return '172.16.' + input_ip
    elif ip_lenth == 3:
        return input_ip
    else:
        logger.error("输入的IP格式不正确")
        sys.exit(1)


if __name__ == '__main__':
    au = r'Basic 2e5bf6aeb6818393a4a430f950f714137e0f02e90b4b76b6cd0aa481dcff64781c8a4e08649b19f11e7894a5e458021c4044d1a0f4a475da3a6fc3ec3a871dd7edcbb9384a0d9e7807f07712e21589fd9aec9f55ab6b68e0a9910152eca2b911c8b1929804d1be960aef942dbd864329619c39a7cf6a95e1a69e1881b5d13f5a8a9bcc295402a6476bd9dcb11cbc3d23e47dbbb7eddfa0dd30faf693f7a487d3'
    # check_ssh_authorization('172.16.70.212', 'cfservice', 'fdfsdf')
    # flexsafe_login('172.16.70.205')
    add_cloud_backup('172.16.71.228:8080', au, 'ace')
