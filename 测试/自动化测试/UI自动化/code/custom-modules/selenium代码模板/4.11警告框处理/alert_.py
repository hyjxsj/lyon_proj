#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import time

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
#鼠标悬停相“设置”链接
link = driver.find_element_by_link_text(u'设置')
ActionChains(driver).move_to_element(link).perform()
#打开搜索设置
driver.find_element_by_class_name('setpref').click()
#保存设置
# ele = driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo')
ele = driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]')
driver.execute_script("arguments[0].click();", ele)

time.sleep(2)

#接收弹窗
driver.switch_to_alert().accept()
# driver.quit()