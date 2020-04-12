#-*- coding:utf8 -*-
__author = "huia"

import urllib.request


url = "https://www.python.org"
response = urllib.request.urlopen(url,timeout=10)
print("响应类型：",type(response))   #响应类型为class，需要调用read方法
print("响应状态码：%s" % response.status)  #响应状态码，成功200，300重定向，400客户端错误，500服务器错误
print("响应头：" ,response.getheaders())  #获取响应头
print("响应头Server信息：",response.getheader('Server'))

