#-*- coding:utf8 -*-
__author = "huia"

import requests

url = "https://www.baidu.com/"
response = requests.get(url)
print(type(response))    #
print(response.status_code) #获取响应的状态码
print(response.text)   #获取响应的内容，unicode格式
print(response.cookies)  #获取响应的cookie

#基本GET请求
#基本写法
response = requests.get('http://httpbin.org/get')
print(response.text)
#带参数GET请求
response = requests.get('http://httpbin.org/get?name=germey&age=22')
print(response.text)

data = {
    'name':'germey',
    'age':'22'
}
url = 'http://httpbin.org/get'
response = requests.get(url,params=data)
