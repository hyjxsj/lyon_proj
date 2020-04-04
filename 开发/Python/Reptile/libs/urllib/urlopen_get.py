#-*- coding:utf8 -*-
__author = "huia"

# urlopen
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

import urllib.request
url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
# print(response.read().decode('utf-8'))
print(type(response))  #responese是一个class
print(response)      #直接打印输出看到，response是一串内存地址
print(response.read())  #通过read读取的内容时候byters类型，需要decode解码一下

