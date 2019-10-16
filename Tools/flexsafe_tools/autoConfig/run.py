# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: run.py
@time: 2019/7/26 9:54
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from loguru import logger

from flexsafe_utils.SSHConnection import SSHConnection

from flexsafe_utils.common import flexsafe_login, config_mail, enable_clock, add_cloud_backup, ssh_login, \
    get_current_time, enable_special_control, parse_ip

input_ip = input('请输入FlexSafe Server IP：172.16.')
host = parse_ip(input_ip)
logger.info("服务器IP:【%s】" % host)

# 同步时间
ssh_info = ssh_login(host)
ssh_name = ssh_info[0]
ssh_passwd = ssh_info[1]
try:
    ssh = SSHConnection(host, 22, ssh_name, ssh_passwd)
    logger.debug('get_current_time:' + get_current_time())
    ssh.exec_command("sudo date -s '{}';".format(get_current_time()), ssh_passwd)
except:
    logger.error('未知错误')
    sys.exit(1)

authorization = flexsafe_login(host)[0]
print('''
功能：

    1.配置邮箱服务器。
    2.开启【加锁功能】、【专用管控功能】。
    3.配置【阿里云】备份服务器。
    4.配置【亚马逊】备份服务器。
    5.配置本地备份服务器。

用法：
    1.使用5位比特码来开启对应选项：
        开启----1
        不开启--0
    2.例如：
        如只开启上方1、3、5功能，请在下方操作指令处输入比特码【10101】
    3.必须为5位的比特码。

''')
input_choice = input('请键入5位的0、1比特码指令：')
if len(input_choice) == 5:
    try:
        int(input_choice)
        if input_choice[0] == '1':
            config_mail(host, authorization)
        if input_choice[1] == '1':
            enable_clock(host, authorization)
            enable_special_control(host, authorization)
        if input_choice[2] == '1':
            add_cloud_backup(host, authorization, 'ace')
        if input_choice[3] == '1':
            add_cloud_backup(host, authorization, 'aws')
        if input_choice[4] == '1':
            current_dir = os.path.dirname(os.path.abspath(__file__))
            backup_tar = os.path.join(current_dir, 'configure_connection.tar.gz')
            host_name_input = input('请输入备份服务器IP：172.16.')
            host_name = '172.16.%s' % host_name_input
            cfback_passwd = input('请输入备份服务器密码（默认为cfbackup）:')
            if cfback_passwd == '':
                cfback_passwd = 'cfbackup'

            try:
                logger.info('正在拷贝配置脚本至【%s】' % host)
                if ssh_name != 'root':
                    ssh.put(backup_tar, '/home/cfservice/configure_connection.tar.gz')
                else:
                    ssh.put(backup_tar, '/root/configure_connection.tar.gz')
                logger.info('正在远程执行脚本，请稍等...')
                ssh.exec_command('cd /home/{ssh_name}/;'
                                 'tar -zxvf configure_connection.tar.gz; '
                                 'cd bak_configure;'
                                 'sudo bash configure_connection.sh {host_name} {cfback_passwd}'
                                 .format(ssh_name=ssh_name, host_name=host_name, cfback_passwd=cfback_passwd),
                                 ssh_passwd)
            except Exception as e:
                logger.error(e)
                logger.error('拷贝配置脚本至【%s】失败！' % host)
    except ValueError:
        logger.error('请键入5位的0、1比特码，不接受其它类型参数！')
        sys.exit(1)
else:
    logger.error('请键入5位的0、1比特码，不接受其它类型参数！')
