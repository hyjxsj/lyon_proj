#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import os
import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()

file_path = "file:///" + os.path.abspath("frame.html")
dr.get(file_path)

#切换到iframe(id = "if")
'''
 switch_to_frame() 默认可以直接取表单的 id 或 name 属性进行切换。如：
#id = "if"
driver.switch_to_frame("if")
#name = "nf"
driver.switch_to_frame("nf")
'''
dr.switch_to_frame("if")

#下面就可以正常的操作元素了
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
time.sleep(3)

dr.quit()