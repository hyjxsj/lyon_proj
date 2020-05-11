# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: run.py
@time: 2019/7/26 11:24
"""
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from loguru import logger
from requests import session

sys.path.append('..')
from flexsafe_utils.common import flexsafe_login, upload_file, parse_ip

print('''
功能：

    1.创建6种读写权限不同的共享目录。
    2.创建2种读写权限不同的存档目录。

''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
my_group_name = input('请输入组名:\n')
host = parse_ip(input_ip)
logger.info("服务器IP:【%s】" % host)
t = flexsafe_login(host)
authorization = t[0]
admin_name = t[1]
admin_paswd = t[2]
group_id = 1

header = {
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": authorization,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


# 创建组
def create_group(group_name):
    base_url = 'http://%s/api/v1/groups' % host
    post_json = {
        "displayName": "",
        "groupName": "",
        "lvName": "/dev/mapper/data-volume",
        "groupTitle": "",
        "privilege": "PRIVATE",
        "fileSystemType": "ext4",
        "creator": "",
        "parentId": "0"
    }
    s = session()
    post_json.update({
        "displayName": group_name,
        "groupName": group_name,
        "groupTitle": group_name,
        "creator": admin_name,
    })
    r = s.post(base_url, headers=header, json=post_json)

    try:
        global group_id
        group_id = json.loads(r.text)['id']
        logger.debug('【group_id】:%s' % group_id)
        logger.info("用户组{%s}----创建成功" % group_name)
        return group_id
    except:
        if 'userMessage' in r.text:

            logger.error("【Error】用户组{%s}创建失败:%s" % (group_name, json.loads(r.text)['userMessage']))
            logger.error("组名已存在，请更换组名！")
            sys.exit(1)

        else:
            logger.error("【Error】用户组{%s}创建失败,原因未知" % group_name)


# 创建共享目录
def create_default_share_dir():
    base_url = 'http://%s/api/v1/sharedirmanager/creatShare' % host
    default_share_dir_list = []
    confirm = input('是否只创建公共模式共享目录？Y/n')

    if confirm == 'y' or confirm == 'Y' or confirm == '':
        default_share_dir_list.append(['2', '_RW_公共共享', '15'])
        default_share_dir_list.append(['2', '_R_公共共享', '0'])
    else:
        default_share_dir_list.append(['2', '_RW_公共共享', '15'])
        default_share_dir_list.append(['2', '_R_公共共享', '0'])
        default_share_dir_list.append(['0', '_RW_主客共享', '15'])
        default_share_dir_list.append(['0', '_R_主客共享', '0'])
        default_share_dir_list.append(['1', '_RW_协作共享', '15'])
        default_share_dir_list.append(['1', '_R_协作共享', '0'])

    for i in default_share_dir_list:
        post_json = {
            "shareTitle": "rere",
            "maxSize": 1,
            "model": "0",
            "groupId": "5",
            "groupPermission": "15",
            "shareType": "GROUP",
            "creator": "admin123"

        }
        post_json.update({
            "shareTitle": 'G_%s%s' % (my_group_name, i[1]),
            "model": i[0],
            "groupId": group_id,
            "groupPermission": i[2],
            "creator": admin_name
        })

        s = session()
        r = s.post(base_url, headers=header, json=post_json)
        if r.status_code == 200:
            logger.info("G_%s%s----创建成功" % (my_group_name, i[1]))
            upload_file(host, authorization, '/%s/%s/' % (my_group_name, post_json['shareTitle']),
                        '%s.txt' % post_json['shareTitle'])
        else:
            logger.error('%s创建失败！' % i[1])
            logger.error(r.text)


# 创建存档目录
def create_default_archieve_dir():
    base_url = 'http://%s/api/v1/archivedirmanager/creatArchive' % host
    default_archieve_dir_list = []
    default_archieve_dir_list.append(['_RW_存档', '5'])
    default_archieve_dir_list.append(['_R_存档', '1'])

    for i in default_archieve_dir_list:
        post_json = {
            "shareName": "ar2",
            "shareType": 1,
            "sharePath": "/flexsafe/data/volume",
            "shareWith": "group.0014",
            "permission": "1",
            "maxSize": 1
        }
        post_json.update({
            "shareName": 'G_%s%s' % (my_group_name, i[0]),
            "shareType": 1,
            "shareWith": "group." + pre_0group(group_id),
            "permission": i[1],
        })

        s = session()
        r = s.post(base_url, headers=header, json=post_json)
        if r.status_code == 200:
            logger.info("G_%s%s----创建成功" % (my_group_name, i[0]))
            upload_file(host, authorization, '/%s/' % (post_json['shareName']), '%s.txt' % post_json['shareName'])
        else:
            logger.error('G_%s创建失败！' % i[1])
            logger.error(r.text)


# 存档用户ID
def pre_0group(id):
    if id < 10:
        return '000' + str(id)
    elif id < 100:
        return '00' + str(id)
    elif id < 1000:
        return '0' + str(id)
    else:
        return str(id)


if __name__ == '__main__':
    archieve_confirm = input('是否创建存档目录？y/N')
    create_group(my_group_name)
    create_default_share_dir()
    if archieve_confirm == 'y' or archieve_confirm == 'Y':
        create_default_archieve_dir()
