#-*- coding:utf8 -*-
__author = "huia"

import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://192.168.0.109:8080/#!/login',auth=('batman','123qwe'))
print(r.status_code)
print(r.url)
print(type(r.cookies))
for key,value in r.cookies.items():
    print(key+"="+value)
print(type(r.text))