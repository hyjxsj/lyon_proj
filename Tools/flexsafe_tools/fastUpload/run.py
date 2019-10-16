# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: demo.py
@time: 2019/5/8 17:40
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from flexsafe_utils.common import check_authorizatin, clear_file_content, split_list, flexsafe_login

current_dir = os.path.dirname(os.path.abspath(__file__))
fail_path = os.path.join(current_dir, 'fail.txt')
file_tree_path = os.path.join(current_dir, 'file_tree.txt')
import json
import threading
import time
from loguru import logger
import requests

from flexsafe_utils.Encrypy import PrpCrypt

logger.add(os.path.join(current_dir, "fastUpload.log"), format="{time} {level} {message}", rotation="5 MB",
           level="DEBUG")
print('''
注意：
    1.程序会自动创建以下组名及对应的共享目录【G_YXT_10000】,【G_YXT_5000】,【G_YXT_2500】,【G_YXT_1250】，
    若待测系统中存在上述组名，请提前进行删除相应组。
    2.由于程序执行时间较长，请使用Linux 的screen命令运行此程序，以保证ssh断开后能保持执行。
    3.【Ctrl+u】撤销输入，而不必【Ctrl+c】中断程序。
    4.输入FlexSafe Server后两段IP地址，按回车继续^_^

''')
input_ip = input('请输入FlexSafe Server IP：172.16.')
# host_name = input_ip
host_name = '172.16.' + input_ip
admin_name = input('请输入FlexSafe Server 管理员账号：')
admin_passwd = input('请输入FlexSafe Server 管理员密码：')
if not check_authorizatin(host_name, admin_name, admin_passwd):
    sys.exit(1)
thread_count = input('请输入上传线程数（建议5-10）：')
g_name_list = ['G_YXT_10000', 'G_YXT_5000', 'G_YXT_2500', 'G_YXT_1250']

pc = PrpCrypt()
authorization = flexsafe_login(host_name)[0]
header = {
    "Authorization": authorization,
}
upload_url = 'http://%s/api/v1/filelists/uploadFile' % host_name


def create_group(group_name):
    logger.info('正在创建所需组和共享目录...')
    # 创建组
    group_id = None
    create_group_url = 'http://%s/api/v1/groups' % host_name
    create_group_post_data = {
        "privilege": "PRIVATE",
        "displayName": group_name,
        "groupName": group_name,
        "lvName": "/dev/mapper/data-volume",
        "groupTitle": group_name,
        "fileSystemType": "ext4",
        "creator": admin_name,
        "parentId": "0"
    }
    r = requests.post(url=create_group_url, json=create_group_post_data, headers=header)
    try:
        group_id = json.loads(r.text)['id']
    except:
        logger.error('''创建组失败，请检查：
                        1.服务器是否可以正常访问
                        2.手动删除已存在用户组：%s
        
        ''' % str(g_name_list))
        is_continue = input("继续请输入Y")
        if is_continue != 'Y':
            sys.exit(1)
    logger.info('创建组【%s】成功！' % group_name)

    # 创建组对应共享目录
    create_dir_url = 'http://%s/api/v1/sharedirmanager/creatShare' % host_name
    create_dir_post_data = {
        "shareTitle": "%s_DIR" % group_name,
        "model": "0",
        "groupPermission": "15",
        "maxSize": 3,
        "groupId": group_id,
        "shareType": "GROUP"
    }
    r = requests.post(url=create_dir_url, json=create_dir_post_data, headers=header)
    try:
        json.loads(r.text)['href']
    except:
        logger.error('【%s】，创建失败' % str(g_name_list))
        is_continue = input("继续请输入Y")
        if is_continue != 'Y':
            sys.exit(1)

    logger.info('创建共享目录【%s_DIR】成功！' % group_name)


def get_file_tree(file_tree):
    with open(os.path.join(current_dir, file_tree), 'r') as f:
        return [x.strip() for x in f.readlines()]


def upload(file_tree):
    post_data = (('userId', '1'),
                 ('isOverWrite', '-1'),
                 ('isSendEmail', 'false'),
                 ('flowChunkNumber', '1'),
                 ('flowChunkSize', '20971520'),
                 ('flowCurrentChunkSize', '1'),
                 ('flowTotalSize', '1'),
                 ('flowTotalChunks', '1'),
                 )

    for i in file_tree:
        fileDir = i.split(r'/')[0].strip()
        fileName = i.split(r'/')[-1].strip()
        if fileDir == '10000':
            post_extra = (('remotePath', '/%s/%s/' % ('G_YXT_10000', 'G_YXT_10000_DIR')),)
            post_data += post_extra
        elif fileDir == '5000':
            post_extra = (('remotePath', '/%s/%s/' % ('G_YXT_5000', 'G_YXT_5000_DIR')),)
            post_data += post_extra
        elif fileDir == '2500':
            post_extra = (('remotePath', '/%s/%s/' % ('G_YXT_2500', 'G_YXT_2500_DIR')),)
            post_data += post_extra
        elif fileDir == '1250':
            post_extra = (('remotePath', '/%s/%s/' % ('G_YXT_1250', 'G_YXT_1250_DIR')),)
            post_data += post_extra

        post_extra1 = (('flowRelativePath', i),)
        post_extra2 = (('flowFilename', fileName),)
        post_extra3 = (('flowIdentifier', '1-' + fileName.replace(' ', '')),)

        r_post = post_data + post_extra1 + post_extra2 + post_extra3
        files = {'file': (fileName, 't', 'text/plain')}
        try:
            time.sleep(2)
            r = requests.post(url=upload_url, files=files, headers=header, data=r_post, timeout=300, verify=False)
            logger.info(r.text + '[{}%]'.format(int((file_tree.index(i) / len(file_tree)) * 100)))
            if 'success' not in r.text:
                with open(fail_path, 'a+') as f:
                    f.write(str(i) + '\n')
        except Exception as e:
            logger.error(e)
            with open(fail_path, 'a+') as f:
                f.write(i + '\n')
            logger.error(files)


if __name__ == '__main__':

    for g_name in g_name_list:
        create_group(g_name)
    clear_file_content(fail_path)
    all_file_tree = get_file_tree(file_tree_path)
    thread_file_tree = split_list(all_file_tree, len(all_file_tree) // int(thread_count.strip()))
    thread_list = []
    logger.info('开始准备上传文件...')
    for i in thread_file_tree:
        threading.Thread(target=upload, args=(i,), daemon=False).start()
