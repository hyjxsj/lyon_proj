# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: run.py
@time: 2019/8/1 9:43
"""
import os
import sys
import time

import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from flexsafe_utils.common import ssh_login

from loguru import logger

from flexsafe_utils.SSHConnection import SSHConnection

current_dir = os.path.dirname(os.path.abspath(__file__))
tar_name = 'rollback.tar.gz'
localpath = os.path.join(current_dir, tar_name)
remotepath = '/home/cfservice/'
print('''
功能：

    1.清空数据表方式还原系统，包括删除管理员。
    2.自动注册管理员账号。

''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
host = '172.16.' + input_ip
logger.warning('【%s】' % host)
logger.warning('【%s】' % host)
logger.warning('【%s】' % host)
logger.warning('【%s】' % host)
logger.warning('【%s】' % host)
logger.warning('【%s】' % host)
logger.warning('【%s】' % host)
logger.warning('请仔细确认上方待清空的IP地址！')
logger.warning('请仔细确认上方待清空的IP地址！')
logger.warning('请仔细确认上方待清空的IP地址！')
confirm = input('将要清空【%s】数据，请确认该IP地址！N/y\n' % host)
logger.debug(confirm)
if confirm != 'y':
    logger.warning('未进行确认操作（小写y确认），程序退出')
    sys.exit(1)
ssh_info = ssh_login(host)
ssh_name = ssh_info[0]
ssh_passwd = ssh_info[1]


def exec_rollback():
    try:
        ssh = SSHConnection(host, 22, ssh_name, ssh_passwd)
    except:
        logger.error('未知错误')
        sys.exit(1)

    ssh.put(localpath, remotepath + '/' + tar_name)
    logger.info('正在执行还原操作...')
    logger.info('正在执行还原操作...')
    logger.info('正在执行还原操作...')
    ssh.exec_command('cd /home/{ssh_name}/;'
                     'tar -zxvf {tar_name}; '
                     'cd rollback;'
                     ' sudo bash iso_rollback.sh'
                     .format(ssh_name=ssh_name, tar_name=tar_name), ssh_passwd)


def register_admin():
    logger.info('还原操作完成，正在注册管理员账号...')
    logger.info('还原操作完成，正在注册管理员账号...')
    logger.info('还原操作完成，正在注册管理员账号...')
    header = {
        "Connection": "close",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Basic",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    base_url = 'http://%s:8080/api/v1/admin' % host
    post_json = {
        "username": "admin123",
        "password": "123qwe",
        "email": "761701732@qq.com"
    }
    while True:
        try:
            r = requests.post(url=base_url, json=post_json, headers=header, timeout=None)
            logger.debug(r.text)
            if (r.status_code == 200):
                logger.info('管理员注册成功【%s】【%s】' % (post_json['username'], post_json['password']))
                break
        except:
            time.sleep(1)
            continue


if __name__ == '__main__':
    exec_rollback()
    register_admin()
