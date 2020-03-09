#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"
import time

from selenium import webdriver
#引入Keys模块
from selenium.webdriver.common.keys import Keys

num = 1
def _sleep(cls):
    time.sleep(cls)

dr = webdriver.Chrome()
dr.get("http://wwww.baidu.com")
#输入框输入内容
dr.find_element_by_xpath('//*[@id="kw"]').send_keys("seleniumm")
_sleep(num)
#删除多输入的一个m
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.BACK_SPACE)
_sleep(num)

#输入空格键 + “教程”
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.SPACE)
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(u"教程")
_sleep(num)

#Ctr + A 全选输入框内容
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'a')
_sleep(num)

#Ctr + X 剪切输入框内容
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'x')
_sleep(num)

#Ctr + V 粘贴内容到输入框
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'v')
_sleep(num)

#通过键盘回车来代替点击操作
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.ENTER)
_sleep(num)

##其他操作
#Tab
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.TAB)
#Esc
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.ESCAPE)
#F1..F12
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.F1)
dr.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.F12)



dr.quit()

