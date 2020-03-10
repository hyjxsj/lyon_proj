#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

from selenium import webdriver

#para define
url = "https://exmail.qq.com/cgi-bin/loginpage"

dr = webdriver.Chrome()
dr.maximize_window()
dr.get(url)

print("Before login===========")
#打印当前页面的title
title = dr.title
print("登录前的title：%s" % title)

#打印当前页面url
now_url = dr.current_url
print("登录前的url：%s" % now_url)

#企业邮箱登录
dr.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[3]/a[1]').click()
dr.find_element_by_xpath('//*[@id="inputuin"]').send_keys("yangyang.huang@cloudfortdata.com")
dr.find_element_by_xpath('//*[@id="pp"]').send_keys("2wsx@WSX")
dr.find_element_by_xpath('//*[@id="btlogin"]').click()

print("After login===========")
#打印当前页面的title
title = dr.title
print("登录后的title：%s" % title)
#打印当前页面url
now_url = dr.current_url
print("登录前的url：%s" % now_url)
