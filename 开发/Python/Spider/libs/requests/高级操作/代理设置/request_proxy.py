#-*- coding:utf8 -*-
__author = "huia"

import requests
#需要先开启一个代理服务器
proxies = {
  "http": "http://127.0.0.1:9743",
  "https": "https://127.0.0.1:9743",
}

response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)

#代理服务器需要用户密码，使用以下方式
import requests

proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)

#使用socks5代理，需要提前使用pip3 install requests[socks]安装依赖库
import requests

proxies = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks5://127.0.0.1:9742'
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)