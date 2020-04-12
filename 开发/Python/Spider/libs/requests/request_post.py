#-*- coding:utf8 -*-
__author = "huia"

import requests
data = {
    'name': 'germey',
    'age': '22'
}
url = "http://httpbin.org/post"
# response = requests.get(url,data=data)  #未加headers，请求非法
# print(response.text)


#加上headers，请求成功
headers = {
'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.post(url,data=data,headers=headers)
print(response.json())
