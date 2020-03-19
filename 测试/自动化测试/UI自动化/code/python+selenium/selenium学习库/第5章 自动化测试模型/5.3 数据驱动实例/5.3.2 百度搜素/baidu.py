#-*- coding:utf8 -*-
__author = "huia"

import time
from selenium import webdriver
from web_driver_wait2 import WebDriverWait2

file_info = open('info.txt','r')
values = file_info.readlines()
file_info.close()

for search in values:
    driver = webdriver.Chrome()
    WebDriverWait2(driver).implicitly(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.quit()
