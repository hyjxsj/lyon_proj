#-*- coding:utf8 -*-
__author = "huia"

import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*Demo$',content,re.S)   #S可以把.匹配扩展到整个字符串
print(result.group(1))