#-*- coding:utf8 -*-
__author = "huia"

import re

content = "Hello 123 4567 World_This is a Regex Demo"
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())
print(result.span())