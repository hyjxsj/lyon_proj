#-*- coding:utf8 -*-
__author = "huia"

import requests
url = "http://www.jianshu.com"
response = requests.get(url)
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)   #访问的url
print(type(response.history),response.history)  #访问历史
