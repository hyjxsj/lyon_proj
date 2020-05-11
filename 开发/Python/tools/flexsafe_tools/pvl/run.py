"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence
@contact: steinven@qq.com
@software: PyCharm
@file: run.py
@time: 2019/9/24 11:13
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from loguru import logger

logger.add(sys.stdout, level="INFO")
from flexsafe_utils.SSHConnection import SSHConnection
from flexsafe_utils.common import ssh_login, parse_ip

current_dir = os.path.dirname(os.path.abspath(__file__))
tar_name = 'pvl.tar.gz'
localpath = os.path.join(current_dir, tar_name)
remotepath = '/home/cfservice/'
print('''
功能：

    1.自动fdisk划盘
    2.自动lvm划分逻辑卷

''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
host = parse_ip(input_ip)
logger.info("服务器IP:【%s】" % host)
ssh_info = ssh_login(host)
ssh_name = ssh_info[0]
ssh_passwd = ssh_info[1]
try:
    ssh = SSHConnection(host, 22, ssh_name, ssh_passwd)
except:
    logger.error('未知错误')
    sys.exit(1)
ssh.exec_command('cd /home/{ssh_name}/;'
                 'rm -fr ./pvl ./pvl.tar.gz'
                 .format(ssh_name=ssh_name)
                 , ssh_passwd)
ssh.put(localpath, remotepath + '/' + tar_name)
logger.info('正在远程执行脚本，请稍等...')
ssh.exec_command('cd /home/{ssh_name}/;'
                 'tar -zxvf {tar_name}; '
                 'cd pvl;'
                 ' sudo bash pvl.sh'
                 .format(ssh_name=ssh_name, tar_name=tar_name), ssh_passwd)
