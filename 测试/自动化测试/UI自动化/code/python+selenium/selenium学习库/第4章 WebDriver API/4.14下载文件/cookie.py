#-*- coding:utf8 -*-
__author = "huia"

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

#获得cookie
cookie = driver.get_cookies()
print(cookie)

#向cookie的name和value添加会话信息
driver.add_cookie({'name':'key-aaaaa','value':'value-bbbbb'})

#遍历cookies中的name和value信息打印，当然还有上面的添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))
    print("--------------------------")

driver.quit()


'''
webdriver 操作 cookie 的方法有：
 get_cookies() 获得所有 cookie 信息
 get_cookie(name) 返回有特定 name 值有 cookie 信息
 add_cookie(cookie_dict) 添加 cookie，必须有 name 和 value 值  delete_cookie(name) 删除特定(部分)的 cookie 信息
 delete_all_cookies() 删除所有 cookie 信息
'''