#-*- coding:utf8 -*-
__author = "huia"

import re

content = "Extra stings Hello 1234567 World_This is a Regex Demo Extra stings"
result = re.match('Hello.*?(\d+).*?Demo',content)
print("match方法从头匹配结果：",result)
result = re.search('Hello.*?(\d+).*?Demo',content)
print("search方法从头匹配结果：",result)
