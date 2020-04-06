#-*- coding:utf8 -*-
__author = "huia"

import requests
import json

url = "http://httpbin.org/get"
response = requests.get(url)
print(response.text)   #输出是str
print(response.json())  #输出是dict
print(json.loads(response.text))  #上面的json方法就是再封装了load方法
