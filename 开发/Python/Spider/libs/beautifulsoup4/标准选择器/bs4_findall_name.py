#-*- coding:utf8 -*-
__author = "huia"

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

#name
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('ul'))   #根据标签名选择，结果多个时，存储成list
print(soup.find_all('ul')[0])   #根据标签名选择，结果有多个时，按下标获取


for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

print('---'.center(50,'-'))
print(soup.find_all(name='li'))  #name关键参数可以省略