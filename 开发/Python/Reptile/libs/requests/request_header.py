#-*- coding:utf8 -*-
__author = "huia"

import requests
url = "https://www.zhihu.com/explore"
response = requests.get(url)
print(response.text)

#添加headers
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.text)