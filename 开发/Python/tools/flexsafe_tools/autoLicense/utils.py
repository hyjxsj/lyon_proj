# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven-office‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: utils.py
@time: 2019/4/26 16:54
"""
import configparser
import os
import sys
import time

import zmail
from loguru import logger

current_dir = os.path.dirname(os.path.abspath(__file__))

logger.add(os.path.join(current_dir, "AutoLicense.log"), format="{time} {level} {message}", rotation="5 MB",
           level="DEBUG")
logger.level("INFO")


def get_conf_value(section, key):
    conf = configparser.ConfigParser()
    conf.read(os.path.join(current_dir, 'conf.cfg'), encoding='utf-8')
    try:
        r = conf.get(section, key)
    except:
        logger.error("配置文件【%s】不存在，或配置不完整，请检查！" % os.path.join(current_dir, 'conf.cfg'))
        time.sleep(5)
        sys.exit(1)
    return r


def get_latest_mail():
    mail_name = get_conf_value('license', 'mail_name')
    mail_passwd = get_conf_value('license', 'mail_passwd')
    server = zmail.server(mail_name, mail_passwd, config='qq')
    try:
        latest_mail = server.get_latest()
    except:
        logger.error("登陆接收license的邮箱失败，请检查配置")
        time.sleep(5)
        sys.exit(1)
    return latest_mail


if __name__ == '__main__':
    print(get_latest_mail().get('headers').get('Subject'))
