#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import time
import unittest
from run.config import config

def createsuite():
    test_suite = unittest.TestSuite()
    #定义discover参数（代码路径）
    discover = unittest.defaultTestLoader.discover(config.testCase_dir,pattern='test*.py',top_level_dir=None)

    #discover方法筛选出来的测试用例，循环添加到测试套件中
    for testcase_py in discover:
        for testcase in testcase_py:
            test_suite.addTest(testcase)
            print(testcase)
    return  test_suite

    print("111111")

