#-*- coding:utf8 -*-
__author = "huia"

#没有会话维持
import requests
url = "http://httpbin.org/cookies/set/number/123456789"
requests.get(url)
response = requests.get('http://httpbin.org/cookies')
print(response.text)

#有会话维持
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)