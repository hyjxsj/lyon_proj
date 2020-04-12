#-*- coding:utf8 -*-
__author = "huia"

import re

content = "price is $5.00"
result = re.match('price is \$5\.00',content)
print(result)
print(type(result))