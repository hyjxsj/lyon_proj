#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import sys,time
import unittest
from selenium import webdriver
from run.config import config
from web_driver_wait2 import WebDriverWait2

class login(unittest.TestCase):
    def setUp(self):
        """
        自动化初始化，预置数据、打开浏览器等
        """
        self.driver = config.browser_select()
        self.driver.maximize_window()
        self.base_url = config.base_url

    def test_login_success(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(3)
        ele = WebDriverWait2(self.driver,ele_by_xpath='//*[@id="username"]').explicitly(5)
        ele.send_keys("batman")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qwe")
        driver.find_element_by_xpath('//*[@id="login_submit"]').click()
        time.sleep(3)
        self.assertEqual(driver.title,"Flex Safe Web",msg="登录失败")

    def test_login_failed(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        title = driver.title
        print(title)

    def tearDown(self):
        self.driver.quit()

