#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import re
#替换为空
content = "Extra stings Hello 1234567 World_This is a Regex Demo Extra stings"
content = re.sub('(\d+)','',content)
print(content)
#替换匹配字符串为特定字符串，匹配的正则表达式可以加括号或者不加
content = "Extra stings Hello 1234567 World_This is a Regex Demo Extra stings"
content = re.sub('\d+','Replacement',content)
print(content)
