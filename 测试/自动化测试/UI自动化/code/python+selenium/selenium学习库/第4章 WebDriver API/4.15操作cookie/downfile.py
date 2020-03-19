#-*- coding:utf8 -*-
__author = "huia"

import os
from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2) #文件下载路径，0默认，2自定义路径
fp.set_preference("browser.download.manager.showWhenStarting",False) #是否显示开始，Ture 为显示，Flase 为不显示
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
"application/octet-stream") #下载文件的类型

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-2").click()

