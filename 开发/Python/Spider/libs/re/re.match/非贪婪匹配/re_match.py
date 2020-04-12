#-*- coding:utf8 -*-
__author = "huia"

import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+)\s(\w+).*?Demo$',content)
print(result.group())
print(result.group(1,2))   #1,2代表多个时（）里匹配的位置
print(result.span())