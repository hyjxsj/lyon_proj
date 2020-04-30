#-*- coding:utf-8 -*-
__author = "Lukas"

import requests

url = "https://console.amazonaws.cn/s3/bucket/cloudfort-backup-test-7e0d8054e59347b9b4c0d42d1c4b2763/delete?region=cn-north-1"
heards = {
    'Content-Type':' application/json',
    'Origin':' https://console.amazonaws.cn',
    'Referer':' https://console.amazonaws.cn/s3/bucket/cloudfort-backup-test-7e0d8054e59347b9b4c0d42d1c4b2763/delete?region=cn-north-1',
    's3v3':' s3v3',
    'Sec-Fetch-Mode':' cors',
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'x-amz-s3-console-op-id':' 710ff019-2ab4-4251-8d9c-340690d29fee',
    'x-amz-s3-console-op-name':' DeleteBucket',
    'x-amz-s3-console-request-id':' 49e51590-370c-44f6-92f7-f2f5e8a90579',
    'x-xsrf-token':' f5d5fc399b09f7c07549c5f74f38d2e92f511e3b7c3dac58988326891ee28060'
}

data = {
    # 'headers':' {X-Amz-User-Agent: "aws-sdk-js/2.621.0 promise",…}',
    'method':' DELETE',
    'operation':' deleteBucket',
    'params': {},
    'path':' /cloudfort-backup-test-7e0d8054e59347b9b4c0d42d1c4b2763',
    'region':' cn-north-1'
}

response = requests.post(url,data=data)
print('请开始'.center(50,'-'))
print(response.status_code)
print(response.text)