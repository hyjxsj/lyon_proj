#-*- coding:utf8 -*-
__author = "huia"

import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)

import requests
from requests.packages import urllib3
urllib3.disable_warnings()     #不显示未验证的警告
response = requests.get('https://www.12306.cn', verify=False)   #verify是否验证证书
print(response.status_code)

#指定证书
import requests
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)