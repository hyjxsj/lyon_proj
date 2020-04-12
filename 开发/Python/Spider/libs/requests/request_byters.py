#-*- coding:utf8 -*-
__author = "huia"

import requests
url = "https://github.com/favicon.ico"
response = requests.get(url)
print(type(response.text),type(response.content))
print(response.text)
print(response.content)

#获取byters文件保存
response = requests.get(url)
with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()

