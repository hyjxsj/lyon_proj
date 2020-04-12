#-*- coding:utf8 -*-
__author = "huia"

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.page_source)
driver.close()