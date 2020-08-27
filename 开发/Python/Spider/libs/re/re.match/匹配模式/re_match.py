#-*- coding:utf-8 -*-
__author = "huia"

import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
'''
#re.S可以把.匹配扩展到整个字符串,简单点说就是字符串中如果包含换行符\n，
re.S会把换行符当成一个字符串里一部分，
'''

result_ = re.match('^He.*?(\d+).*Demo$',content)
result = re.match('^He.*?(\d+).*Demo$',content,re.S)
try:
    print("没加re.S，结果是：" + result_.group(1))
except (SyntaxError,AttributeError) as e:
    print("没加re.S，没有匹配到，方法错误")
except Exception as e:
    print("未知错误！")
else:
    print("一切正常。")
finally:
    print("不管有没有错都在最后执行。")

print("加上re.S，结果是："+result.group(1))


