#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import time

from selenium import webdriver
from web_driver_wait2 import  WebDriverWait2

dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
ele = WebDriverWait2(dr,3,'//*[@id="kw"]').explicitly()
ele.send_keys("selenium")

time.sleep(1)
dr.quit()
