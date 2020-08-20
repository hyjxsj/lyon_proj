#-*- coding:utf-8 -*-
__author = "Lukas"

import re

str1 = "123abc456opqAA"
def cut_text(text, lenth):
    '''
    text: text parm is string
    lenth: lenth cut
    '''
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    return textArr

ok=cut_text(str1,3)
for i in range(len(ok)):
    print(i,ok[i])