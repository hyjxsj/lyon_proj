#-*- coding:utf8 -*-
__author = "huia"

import xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('info.xml')

#得到文档元素对象
root = dom.documentElement
tagname=root.getElementsByTagName('maxid')
print(tagname[0].tagName)
print(tagname[2].tagName)
print(tagname[1].tagName)