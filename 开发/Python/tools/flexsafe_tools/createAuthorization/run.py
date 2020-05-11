# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 
@software: PyCharm
@file: run.py
@time: 2019/5/13 22:40
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from flexsafe_utils.Encrypy import PrpCrypt
from loguru import logger

current_dir = os.path.dirname(os.path.abspath(__file__))
pc = PrpCrypt()
name_prefix = input('请输入用户名前缀(如“yxt”)：')
user_interval = input('请输入用户区间以"-"分割(如“1-30”)：')

user_start = int(user_interval.split('-')[0])
try:
    user_end = int(user_interval.split('-')[1])
    verify = input(
        '用户名区间：' + name_prefix + '_' + str(user_start) + '--->' + name_prefix + '_' + str(user_end) + '，\nY确认该操作')
    if verify == 'y' or verify == 'Y':
        result_path = os.path.join(current_dir, 'Authorization.txt')
        if (os.path.exists(result_path)):
            with open(result_path, 'w') as f:
                f.truncate()
        for i in range(user_start, user_end + 1):
            r = pc.create_Authorization(name_prefix + '_' + str(i), '123qwe')
            print(r)
            with open(result_path, 'a') as f:
                f.writelines(r + '\n')
        logger.warning('以保存至：【%s】' % result_path)
    else:
        logger.info('未确认，程序退出！')
except:
    logger.error('请输入正确区间，以“-”分割，如“1-30”')
