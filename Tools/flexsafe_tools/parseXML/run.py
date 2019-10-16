# encoding: utf-8
"""
@version: python3.6
@author: ‘steinven‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: demo.py
@time: 2019/7/17 16:03
"""
import os
import time
import xml.dom.minidom as xmldom

print('''
功能：提取xml自动化结果的失败用例，用于重跑。
使用方法：将xml文件拖进此窗口，回车执行。结果输出至xml所在路径，与xml文件同名的txt文件
''')

xml_file = input('拖拽xml文件至此处\n')
(filepath, tempfilename) = os.path.split(xml_file)
tempfilename = tempfilename.replace('xml', 'txt')
r = set()

if (os.path.exists(os.path.join(filepath, tempfilename))):
    os.remove(os.path.join(filepath, tempfilename))
# 得到文档对象
try:
    domobj = xmldom.parse(os.path.abspath(xml_file))
    # 得到元素对象
    elementobj = domobj.documentElement

    # 获得子标签
    allSuits = elementobj.getElementsByTagName("suite")
    for suit in allSuits:
        for test in suit.getElementsByTagName("test"):
            if test.getAttribute('status') != 'passed' and (
                    'Process' in test.getAttribute('name') or 'process' in test.getAttribute('name')):
                r.add('''<class name="''' + test.getAttribute('locationUrl').split('/')[2] + '''"/>\n''')

    # 为了有序输出，将set转为list
    s2l = list(r)
    s2l.sort()
    with open(os.path.join(filepath, tempfilename), 'a') as f:
        for i in s2l:
            f.write(i)

    print("对应文件已生成在xml文件所在目录，为同名txt文件，请检查，3秒后关闭")
    time.sleep(3)
except:
    print('1.请拖入正确格式的xml文件！\n')
    print('2.请不要使用特殊字符命名xml文件！\n')
    time.sleep(5)
