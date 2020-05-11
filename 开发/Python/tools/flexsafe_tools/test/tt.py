"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence
@contact: steinven@qq.com
@software: PyCharm
@file: tt.py
@time: 2019/9/27 9:37
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from loguru import logger

from flexsafe_utils.SSHConnection import SSHConnection
from flexsafe_utils.common import ssh_login

host = '172.16.71.168'
ssh_info = ssh_login(host)
ssh_name = ssh_info[0]
ssh_passwd = ssh_info[1]

host_name = '172.16.71.168'
cfback_passwd = 'cfbackup'

try:
    ssh = SSHConnection(host, 22, ssh_name, ssh_passwd)
except:
    logger.error('未知错误')
    sys.exit(1)
local_dir_name = 'bak_configure'
current_dir = os.path.dirname(os.path.abspath(__file__))
localpath = os.path.join(current_dir, local_dir_name)
ssh.put(localpath, '/home/cfservice/' + local_dir_name)
# ssh.exec_command('cd /home/{ssh_name}/;'
#                  'sudo rm -fr /root/.ssh;'
#                  'sudo tar -zxvf {tar_name} -C /root/; '
#                  .format(ssh_name=ssh_name, tar_name=tar_name, host_name=host_name, cfback_passwd=cfback_passwd),
#                  ssh_passwd)
