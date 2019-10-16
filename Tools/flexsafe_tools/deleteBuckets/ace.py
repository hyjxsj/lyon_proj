# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: my_test.py
@time: 2019/5/5 11:28
"""

# -*- coding: utf-8 -*-
import os
import sys

import oss2
from loguru import logger

current_dir = os.path.dirname(os.path.abspath(__file__))
OSS_KEY = 'LTAIdDa0FSnWHAO9'
OSS_SECRET = 'yNqeNPxypxsV7zBaZt4gAaZNRIxxDM'
OSS_HOST = 'oss-cn-shanghai.aliyuncs.com'
auth = oss2.Auth(OSS_KEY, OSS_SECRET)
logger.add(os.path.join(current_dir, "bucketDelete.log"), format="{time}|{level}|{message}", rotation="5 MB",
           level="DEBUG")


def get_all_buckets_name():
    logger.info('--------获取所有【bucket name】--------')
    service = oss2.Service(auth, OSS_HOST)
    return [info.name for info in oss2.BucketIterator(service)]


def get_bucket(bucket_name):
    logger.info('--------获取【bucket】实例--------')
    return oss2.Bucket(oss2.Auth(OSS_KEY, OSS_SECRET), OSS_HOST, bucket_name)


def get_bucket_all_files(bucket):
    logger.info('--------获取【bucket】下【所有文件】--------')
    return [obj.key for obj in oss2.ObjectIterator(bucket, delimiter='/')]


def delete_files(bucket, file_list):
    logger.info('--------删除【bucket】下【所有文件】--------')
    result = bucket.batch_delete_objects(file_list)
    # 打印成功删除的文件名。
    logger.info('--------删除【bucket】下【所有文件】--------')
    logger.info('\n'.join(result.deleted_keys))


def delete_bucket(bucket):
    logger.info('--------删除【bucket】--------')
    try:
        # 删除存储空间。
        bucket.delete_bucket()
    except oss2.exceptions.BucketNotEmpty:
        print('bucket is not empty.')
    except oss2.exceptions.NoSuchBucket:
        print('bucket does not exist')


def ace_run():
    choice = input('是否删除阿里云账号【安城数据专用】【所有】Bucket？确认请输入【Y】\n' * 3)
    if choice == 'Y':
        all_bk_name = get_all_buckets_name()
        if len(all_bk_name) == 0:
            logger.warning("已清空阿里云账号【安城数据专用】所有Bucket！")
            logger.warning("已清空阿里云账号【安城数据专用】所有Bucket！")
            logger.warning("已清空阿里云账号【安城数据专用】所有Bucket！")
            sys.exit(1)
        for bk_name in all_bk_name:
            bucket = get_bucket(bk_name)
            for i in range(2000):
                all_file_list = get_bucket_all_files(bucket)
                if len(all_file_list) != 0:
                    delete_files(bucket, all_file_list)
                else:
                    break
            delete_bucket(bucket)
        logger.info("已清空阿里云账号【安城数据专用】所有Bucket！")
        logger.info("已清空阿里云账号【安城数据专用】所有Bucket！")
        logger.info("已清空阿里云账号【安城数据专用】所有Bucket！")
        sys.exit(1)
    else:
        logger.error("未执行确认操作，程序退出~")
        logger.error("未执行确认操作，程序退出~")
        logger.error("未执行确认操作，程序退出~")
        sys.exit(1)


if __name__ == '__main__':
    ace_run()
