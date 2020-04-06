#-*- coding:utf8 -*-
__author = "huia"

import urllib.request
url = "https://python.org"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
