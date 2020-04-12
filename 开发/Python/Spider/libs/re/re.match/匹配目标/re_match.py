#-*- coding:utf8 -*-
__author = "huia"

import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+).*Demo$',content)
print(result.group())
print(result.group(1))
print(result.groups())
print(result.span())