#-*- coding:utf-8 -*-
__author = "Lukas"

import requests

ip = "172.16.71.182"
url = "http://{ip}:8080/api/v1/filelists/uploadFile".format(ip=ip)
header = {
    "Authorization" : "Basic dc7fafe1db0a9a22f9a1eed08d6c31e7742d3f4ee7aa\
    5398fc941169ba2512611533bf5ced0bbf82a08f98b5eeb55c1a9d8b6b98fae1eda8b\
    63da9f7e85765864cb88ac203a06aa137426d14ff10789294f4d7fe282a1473264af8\
    29b664e482362e7787fbe9ed1cf556e434cdbf18d84fc180c9933b250fe63c441fb93\
    7424ef5a55bad2cba7bb7364f9c693928a22ba9420a21c8ea7d63d0977d8d520000dc",
}
files = {
    # 'img':('gf.jpg',open('gf.jpg','rb'),'image/jpeg',{}),
    'img': open("gf.jpg",'rb')
}
data = {
    'userId': 2,
    'remotePath': '/',
    'isOverWrite': -1,
    'isSendEmail': 'false',
    'flowChunkNumber': 1,
    'flowChunkSize': 20971520,
    'flowCurrentChunkSize': 27474,
    'flowTotalSize': 27474,
    'flowIdentifier': '27474-gfjpg',
    'flowFilename': 'gf.jpg',
    'flowRelativePath': 'gf.jpg',
    'flowTotalChunks': 1
}
res = requests.post(url,headers=header,data=data,files=files)
print(res.text)