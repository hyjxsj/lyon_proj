#-*- coding:utf8 -*-
__author = "huia"

import urllib.request

#使用urlencode
url = "http://httpbin.org/get"
response = urllib.request.urlopen(url,timeout=10)
print(response.read())