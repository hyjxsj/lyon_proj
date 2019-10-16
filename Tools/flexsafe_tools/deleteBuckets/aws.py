# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: test.py
@time: 2019/5/6 10:36
"""
import os
import sys

import boto3
from loguru import logger

current_dir = os.path.dirname(os.path.abspath(__file__))

region_name = 'cn-north-1'
aws_access_key_id = 'AKIAPYYWDIHERMC6R6QA'
aws_secret_access_key = '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'
client = boto3.client(region_name=region_name,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      service_name='s3')
s3 = boto3.resource(region_name=region_name,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    service_name='s3')


def get_test_bucket_name():
    r = []
    buckets = s3.buckets.filter(Prefix="cloudfort")
    for bucket in buckets:
        if bucket.name.startswith('cloudfort-backup'):
            r.append(bucket.name)
    return r


def get_buckets_from_file():
    with open('aws_buckets.txt', 'r')as f:
        return [x.strip() for x in f.readlines()]


# 删除bucket
def delete_bucket(bucket_name):
    logger.info('正在删除bucket：%s' % bucket_name)
    client.delete_bucket(Bucket=bucket_name)


# 根据bucket名获取bucket
def get_bucket_by_name(name):
    bucket = s3.Bucket(name)
    return bucket


def delete_file(bucket):
    object_summary_iterator = bucket.objects.all()
    try:
        for obj in object_summary_iterator:
            logger.info('正在删除文件对象：【%s】' % obj)
            response = bucket.delete_objects(
                Delete={
                    'Objects': [
                        {
                            'Key': obj.key,
                        },
                    ],
                },
            )
            print(response)
    except:
        logger.error("bucket不存在，请重新填写[aws_buckets.txt]配置文件！")
        sys.exit(1)


def aws_run():
    logger.info('正在删除AWS账号【cf-s3-dev】中测试Bucket...')
    logger.info('正在删除AWS账号【cf-s3-dev】中测试Bucket...')
    logger.info('正在删除AWS账号【cf-s3-dev】中测试Bucket...')

    bucket_names = get_test_bucket_name()
    if len(bucket_names) == 0:
        logger.info('未获取到测试Bucket,请登录Web确认！')
        sys.exit(1)
    logger.warning('已获取到以下测试Bucket，输入Y确认删除,请仔细确认！！！！')
    logger.warning('已获取到以下测试Bucket，输入Y确认删除,请仔细确认！！！！')
    logger.warning('已获取到以下测试Bucket，输入Y确认删除,请仔细确认！！！！')
    for bucket_name in bucket_names:
        logger.info(bucket_name)
    choice = input()
    if choice == 'Y':
        for bucket_name in bucket_names:
            if 'cloudfort-backup' in bucket_name:
                bucket_intance = get_bucket_by_name(bucket_name)
                delete_file(bucket_intance)
                delete_bucket(bucket_name)
            else:
                logger.error("Bucket:%s,貌似不是测试Bucket，请检查！如需继续，请前往Web界面进行操作！" % bucket_name)
    else:
        logger.error("未执行确认操作，程序退出~")
        logger.error("未执行确认操作，程序退出~")
        logger.error("未执行确认操作，程序退出~")
        sys.exit(1)


if __name__ == '__main__':
    aws_run()
