#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import HTMLTestRunner
from ..config import config
from run.tools import createsuite
from . import send_email

suite = createsuite.createsuite()
def runner():
    fp = open(config.report_FileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title=u'【模板】-测试报告',
        description=u'用例执行情况：')
    runner.run(suite)
    fp.close()

    #发送邮件
    send_email.send_email()