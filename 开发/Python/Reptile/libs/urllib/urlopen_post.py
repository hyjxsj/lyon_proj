#-*- coding:utf8 -*-
__author = "huia"

import urllib.parse
import urllib.request

#使用urlencode
data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
url = "http://httpbin.org/post"
response = urllib.request.urlopen(url,data=data)
print(response.read())