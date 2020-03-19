#-*- coding:utf8 -*-
__author = "huia"

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
try:
    driver.find_element_by_id('kw_error').send_key('selenium')
    driver.find_element_by_id('su').click()
except :
    driver.get_screenshot_as_file("D:\\baidu_error.png")
    driver.quit()