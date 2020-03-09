#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
#打开上传页面
file_path = "file:///" + os.path.abspath("upfile.html")
print(file_path)
driver.get(file_path)

#定位上传按钮，添加本地文件
driver.find_element_by_name('file').send_keys("D:\\Workstation\\Code\\Python\\Pytho3.5\\Python_study\\Workstation\\Workspace\\autotest_template\\4.12上传文件\\upfile.html")