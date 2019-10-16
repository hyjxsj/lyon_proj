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
# 创建用户
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import threading
from urllib import parse

from flexsafe_utils.SSHConnection import SSHConnection
import webdav.client as wc

from flexsafe_utils.common import flexsafe_login, split_list, ssh_login, excuseSQL

import json

from loguru import logger
from requests import session

print('''
主要功能：
         1.快速删除所有【用户】、【用户组及项目组】、【共享目录】、【存档目录】
''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
host = '172.16.' + input_ip
ssh_account = ssh_login('172.16.' + input_ip)
authorization = flexsafe_login(host)[0]
header = {
    "Host": host,
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": authorization,
    "channel": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


# 删除除了staff所有组（包括项目组）
def delete_sub_group(g_id):
    url = 'http://{}/api/v1/groups/batchDeleteGroups/{}/true'.format(host, parse.quote(str(g_id)))
    logger.debug(url)
    logger.info("正在删除所有组...")
    r = session().delete(url=url, headers=header)
    logger.info(r.text)


# 获取所有用户
def get_all_users():
    url = 'http://{}/api/v1/users/getAllUsers/1/1'.format(host)
    logger.debug(url)
    logger.info("正在获取第1页用户...")
    r = session().get(url=url, headers=header)
    r_d = json.loads(r.text)
    users = list(r_d['items'][0])
    page = r_d['items'][1]
    logger.debug("page:%s" % page)
    if len(page) > 1:
        for i in range(2, len(page) + 1):
            url = 'http://{}/api/v1/users/getAllUsers/{}/1'.format(host, i)
            logger.debug(url)
            logger.info("正在获取第{}页用户...".format(i))
            r = session().get(url=url, headers=header)
            r_d = json.loads(r.text)
            users += (r_d['items'][0])

    return users


# 删除指定用户
def del_user(user_list):
    for user in user_list:
        url = 'http://{}/api/v1/users/batchDeleteUsers/{}/true?userId='.format(host,
                                                                               parse.quote(str('[%s]' % user['id'])))
        r = session().delete(url=url, headers=header)
        logger.info('正在删除【%s】' % user['id'])
        # logger.info(r.text)


# 删除共享目录
def del_share_dir(dir_id_list):
    for dir_id in dir_id_list:
        url = 'http://{}/api/v1/sharedirmanager/deleteOneShare/{}'.format(host, dir_id)

        r = session().delete(url=url, headers=header)
        logger.info('正在删除【%s】' % dir_id)
        logger.info(r.text)


# 删除存档目录
def del_archieve():
    # 只考虑share_path为/flexsafe/data/volume的情况
    logger.info('正在删除存档文件')
    share_path = '/flexsafe/data/volume/'
    share_names = excuseSQL(host, ssh_account, 'flexsafe', '''SELECT share_name FROM flexsafe.archive_dir;''')
    ssh = SSHConnection(host, 22, ssh_account[0], ssh_account[1])
    options = {
        'webdav_hostname': "http://%s/remote.php/webdav" % host,
        'webdav_login': "admin123",
        'webdav_password': "123qwe"
    }
    client = wc.Client(options)
    for share_name in share_names:
        print(client.clean('%s/' % share_name))
        ssh.exec_command('sudo chattr -R -i %s%s/*' % (share_path, share_name), ssh_account[1])
        ssh.exec_command('sudo rm -fr %s%s' % (share_path, share_name), ssh_account[1])

    logger.info('正在清空Flexsafe存档相关表【archive_dir】')
    excuseSQL(host, ssh_account, 'flexsafe', '''TRUNCATE TABLE archive_dir;''')


if __name__ == '__main__':
    logger.warning('请键入数字选项，执行对应操作！')
    logger.warning('数据删除操作，请谨慎执行，请仔细确认服务器IP！！！！')
    logger.warning('数据删除操作，请谨慎执行，请仔细确认服务器IP！！！！')
    logger.warning('数据删除操作，请谨慎执行，请仔细确认服务器IP！！！！')
    logger.info('1.删除【所有用户、所有用户组及项目组】')
    logger.info('2.删除【所有共享目录】')
    logger.info('3.删除【所有存档】')
    logger.info('4.删除【以上所有】')
    # choice = input()
    choice = '4'

    if choice == '1':
        # 删除所有用户组
        g_id = excuseSQL(host, ssh_account, 'flexsafe',
                         '''SELECT id FROM `flexsafe`.`groups` WHERE display_name!="staff"''')
        excuseSQL(host, ssh_account, 'flexsafe', '''DELETE FROM groups WHERE display_name!="staff";''')
        delete_sub_group(g_id)

        # 删除所有用户
        all_user = get_all_users()
        logger.debug("all_user:%s" % all_user)
        if len(all_user) >= 3:
            s_user_list = split_list(all_user, len((all_user)) // 3)
            for i in s_user_list:
                threading.Thread(target=del_user, args=(i,), daemon=False).start()
        else:
            del_user(all_user)

    elif choice == '2':
        # 删除所有共享目录
        all_dir = excuseSQL(host, ssh_account, 'flexsafe', '''SELECT id FROM `flexsafe`.`share_dir`''')
        logger.debug("all_dir:%s" % all_dir)
        if len(all_dir) >= 3:
            s_dir_list = split_list(all_dir, len((all_dir)) // 3)
            for i in s_dir_list:
                threading.Thread(target=del_share_dir, args=(i,), daemon=False).start()
        else:
            del_share_dir(all_dir)

    elif choice == '3':
        # 删除所有存档
        del_archieve()

    elif choice == '4':
        # 删除所有用户组
        g_id = excuseSQL(host, ssh_account, 'flexsafe',
                         '''SELECT id FROM `flexsafe`.`groups` WHERE display_name!="staff"''')
        excuseSQL(host, ssh_account, 'flexsafe', '''DELETE FROM groups WHERE display_name!="staff";''')
        if len(g_id) >= 3:
            g_id_list = split_list(g_id, len((g_id)) // 3)
            for i in g_id_list:
                threading.Thread(target=delete_sub_group, args=(i,), daemon=False).start()
        else:
            delete_sub_group(g_id)
        delete_sub_group(g_id)

        # 删除所有用户
        all_user = get_all_users()
        logger.debug("all_user:%s" % all_user)
        if len(all_user) >= 3:
            s_user_list = split_list(all_user, len((all_user)) // 3)
            for i in s_user_list:
                threading.Thread(target=del_user, args=(i,), daemon=False).start()
        else:
            del_user(all_user)

        # 删除所有共享目录
        all_dir = excuseSQL(host, ssh_account, 'flexsafe', '''SELECT id FROM `flexsafe`.`share_dir`''')
        logger.debug("all_dir:%s" % all_dir)
        if len(all_dir) >= 3:
            s_dir_list = split_list(all_dir, len((all_dir)) // 3)
            for i in s_dir_list:
                threading.Thread(target=del_share_dir, args=(i,), daemon=False).start()
        else:
            del_share_dir(all_dir)

        # 删除所有存档
        del_archieve()
    else:
        logger.info("程序退出~")
