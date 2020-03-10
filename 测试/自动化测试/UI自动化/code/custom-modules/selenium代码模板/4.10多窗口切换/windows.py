#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import time
from selenium import webdriver
from web_driver_wait2 import WebDriverWait2

url = "http://www.baidu.com"
driver = webdriver.Chrome()
WebDriverWait2(driver).implicitly(3)
driver.get(url)

#获取百度搜索窗口句柄
search_windows = driver.current_window_handle
driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_link_text(u"立即注册").click()

#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

#进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to_window(handle)
        print('now register window!')
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('username')
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys('password')
        #……

#进入搜索窗口
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to_window(handle)
        print('now sreach window!')
        driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(5)