#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import time
import unittest
import HTMLTestRunner
from test_project.tools import send_email
from test_project.config import config

def createsuit():
    test_suite = unittest.TestSuite()
    # 定义测试文件查找的目录
    # 定义discover 方法的参数
    discover = unittest.defaultTestLoader.discover(config.testCode_dir,pattern='test*.py',top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_module in discover:
        for test_case in test_module:
            test_suite.addTests(test_case)
            print(test_suite)
    return test_suite


if __name__ == '__main__':
    # alltestnames = createsuit()
    fp = open(config.report_FileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'【模板】-测试报告',
        description=u'用例执行情况：')
    # runner.run(alltestnames)    #经测试，此种方式调用不生成测试报告
    runner.run(createsuit())
    fp.close()

    #测试报告发送邮件
    send_email.send_email()


