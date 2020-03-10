#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import sys,time
import unittest
from selenium import webdriver
# from ....config import config

class testcase1(unittest.TestCase):
    def setUp(self):
        """
        自动化初始化，预置数据、打开浏览器等
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # self.base_url = config.base_url
        self.base_url = "http://www.baidu.com"

    def testcase1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        print("\n----------end")

    def tearDown(self):
        pass

