# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: ttt.py
@time: 2019/5/6 15:52
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from loguru import logger

from deleteBuckets.ace import ace_run
from deleteBuckets.aws import aws_run

if __name__ == '__main__':
    choice = input('''
    请输入操作选项：
    0----->清空阿里云Bucket
    1----->清空亚马逊Bucket
    2----->退出
    ''')
    if choice == '0':
        ace_run()
    elif choice == '1':
        aws_run()
    else:
        logger.error("正在退出~")
        logger.error("正在退出~")
        logger.error("正在退出~")
        sys.exit(1)
