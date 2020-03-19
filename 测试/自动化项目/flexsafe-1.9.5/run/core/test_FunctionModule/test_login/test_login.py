#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import sys,time
import unittest
from selenium import webdriver
from ....config import config

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
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("batman")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qwe")
        driver.find_element_by_xpath('//*[@id="login_submit"]').click()
        
        time.sleep(3)
        print("\n----------end")

    def tearDown(self):
        self.driver.quit()

