#-*- coding:utf8 -*-
__author = "huia"

import requests
url = "https://www.baidu.com"
response = requests.get(url)
print(response.cookies)
print(type(response.cookies))
for key,value in response.cookies.items():    #items()把字典dict装换成列表list
    print(key + '=' + value)

