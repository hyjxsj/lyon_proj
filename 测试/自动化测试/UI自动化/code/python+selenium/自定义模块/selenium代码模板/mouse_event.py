#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

#鼠标单击
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("[目标URL地址]")
dr.find_element_by_xpath('[元素定位]').click()

#鼠标双击
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #ActionChains是类名
dr = webdriver.Chrome()
dr.get("[目标URL地址]")
ele = dr.find_element_by_xpath('[元素定位]')
ActionChains(dr).context_click(ele).perform()

#鼠标悬停
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("[目标URL地址]")
ele = dr.find_element_by_xpath('[元素定位]')
ActionChains(dr).move_to_element(ele).perform()

#鼠标双击
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("[目标URL地址]")
ele = dr.find_element_by_xpath('[元素定位]')
ActionChains(dr).double_click(ele).perform()

#鼠标推放操作
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("[目标URL地址]")
ele_src = dr.find_element_by_xpath('[元素定位]')
ele_target = dr.find_element_by_xpath('[元素定位]')
ActionChains(dr).drag_and_drop(ele_src,ele_target).perform()

#

