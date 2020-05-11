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
import base64
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from flexsafe_utils.Encrypy import PrpCrypt
from flexsafe_utils.common import flexsafe_login, get_flexsafe_version, config_mail, enable_clock, is_new_version, \
    parse_ip

import json
import random
import time

from loguru import logger
from requests import session

prpCrypt = PrpCrypt()
legal_user = []
print('''
注意：

    1.尽量避免多个用户同时使用本程序，否则可能会导致创建用户失败或其他错误！
    2.建议一次性创建完所有用户，然后根据用户序号分配给相关测试人员。
    3.用户创建完成后，会自动登录，以产生【个人文件夹】，所以可以直接登录Windows Client。
    4.注意输出日志，若有错误，及时反馈。
    5.默认创建用户的密码为【123qwe】,空间大小为2GB。
    6.【Ctrl+u】撤销输入，而不必【Ctrl+c】中断程序。
    7.输入FlexSafe Server后两段IP地址，按回车继续^_^


''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
host = parse_ip(input_ip)
logger.info("服务器IP:【%s】" % host)

flexsafe_version = get_flexsafe_version(host)
authorization = flexsafe_login(host)[0]
if authorization == None:
    logger.error("获取认证失败，请检查Flexsafe服务是否正常！")
    sys.exit(1)
s = session()
header = {
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": '',
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


# 获取要生成的用户名list
def user_name_list():
    name_prefix = input('请输入用户名前缀(如“yxt”)：')
    choice = input('创建用户完成后，是否设置邮箱服务器，开启加锁功能？(N/y)')
    if choice == 'y' or choice == 'Y':
        config_mail(host, authorization)
        enable_clock(host, authorization)
    user_count = input('请输入创建用户数(默认创建1个)：')
    if user_count == '':
        user_count = 1
    return [name_prefix + '_' + str(x) for x in range(0, (int(user_count)))]


# 修改用户密码
def change_user_passwd(user_name):
    base_url = 'http://%s/api/v1/authentication' % host

    post_json = {
        "password": "",
        "newPassword": ""
    }

    logger.info('【%s】修改密码中' % user_name)
    passwd = '123qwe'

    if not is_new_version(host):
        authorization = 'Basic ' + bytes.decode(base64.b64encode(str.encode(user_name + ':' + passwd)))
        header.update({
            'Authorization': authorization,
        })
        post_json.update({
            'password': passwd,
            'newPassword': passwd,
        })
    else:
        header.update({
            'Authorization': prpCrypt.create_Authorization(user_name, passwd),
        })
        post_json.update({
            'password': prpCrypt.encrypt(prpCrypt.md5(passwd)).decode('utf-8'),
            'newPassword': prpCrypt.encrypt(passwd).decode('utf-8'),
        })
    s = session()
    r = s.put(base_url, headers=header, json=post_json)
    if r.status_code == 200:
        logger.info("【%s】密码修改成功" % user_name + '*' * 2)
    else:
        logger.error("【%s】密码修改失败" % user_name)
        logger.debug(r.text)


# 请求首次登陆接口，使之生成【个人文件夹】目录
def user_first_login(user_id):
    url = 'http://%s/api/v1/users/quota/%s' % (host, user_id)
    r = session().get(url=url, headers=header)
    if r.status_code == 200:
        return True
    else:
        logger.debug(r.text)


# 创建用户
def create_user(u_name_list):
    user_size = input('请输入用户空间大小（默认2GB）：')
    global legal_user
    base_url = 'http://%s/api/v1/users?userId=' % host
    post_json = {
        "username": "",
        "email": "",
        "password": "",
        "lvName": "/dev/mapper/data-volume",
        "userTitle": "",
        "department": "",
        "phone": "",
        "personalName": "",
        "sendemailornot": "false",
        "maxSize": 1,
        "privilege": "READWRITE",
        "duty": 2,
        "fileSystemType": "ext4"
    }

    header.update({
        'Authorization': authorization,
    })
    for i in u_name_list:
        logger.info('用户【%s】创建中' % i)
        if user_size == '':
            user_size = 2
        post_json.update({
            'username': i,
            'email': str(random.randint(1000000, 999999999)) + '@cloudfortdata.com',
            'password': '123qwe',
            'userTitle': i,
            'maxSize': user_size,
        })
        time.sleep(2)
        r = s.post(base_url, headers=header, json=post_json)
        if r.status_code == 200:
            logger.info('*' * 2 + "【%s】创建成功" % i + '*' * 2)
            change_user_passwd(i)
            user_id = json.loads(r.text)['id']
            # logger.info(i + '[id]:' + str(json.loads(r.text)['id']))
            if not user_first_login(user_id):
                logger.error('【%s】登陆失败，请手动登陆！' % i)
            else:
                logger.info('【%s】登陆成功！' % i)
        else:
            try:
                dict_s = json.loads(r.text)
                logger.error("【%s】创建失败!:%s" % (i, dict_s['userMessage']))
            except:
                logger.error("【%s】创建失败!:%s" % (i, '原因未知'))
                logger.debug(r.text)

    return legal_user


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    u_name_list = user_name_list()
    create_user(u_name_list)
    logger.info("所有用户创建完成！")
