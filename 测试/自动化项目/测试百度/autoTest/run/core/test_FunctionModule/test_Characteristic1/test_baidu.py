#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import sys,time
import unittest
from selenium import webdriver
from ....config import config

class testcase1(unittest.TestCase):
    def setUp(self):
        """
        自动化初始化，预置数据、打开浏览器等
        """
        self.driver = config.browser_select()
        self.driver.maximize_window()
        # self.base_url = config.base_url
        self.base_url = "http://www.baidu.com"

    def testcase1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys("123")
        driver.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(2)
        self.assertEqual(u"123_百度搜索",driver.title)

    def tearDown(self):
        pass

