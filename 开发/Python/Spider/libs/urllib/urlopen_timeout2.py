#-*- coding:utf8 -*-
__author = "huia"

import socket
import urllib.response
import urllib.error

url = "http://httpbin.org/get"
try:
    response = urllib.request.urlopen(url,timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("Time out !")