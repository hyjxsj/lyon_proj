# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 
@software: PyCharm
@file: demo.py
@time: 2019/5/12 23:33
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from loguru import logger

from flexsafe_utils.SSHConnection import SSHConnection
from flexsafe_utils.common import ssh_login, get_current_time, parse_ip

print('''
功能：

    1.自动与172.16.71.180服务器同步时间。
    
''')
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
    logger.info('设置成功，【%s】当前时间为【%s】' % (host, get_current_time()))
except:
    logger.error('未知错误')
    sys.exit(1)
