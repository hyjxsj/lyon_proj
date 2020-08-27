#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"
import time
from selenium import webdriver

"""
此配置文件用来统一配置自动化测试用例的路径，
环境变量等
"""

#all dir config
#testcase dir
testCase_dir = u"D:\\Code\\Github\\Lukas_proj\\测试\\自动化项目\\flexsafe-1.9.5\\run\\core"
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_FilePath = u"D:\\Code\\Github\\Lukas_proj\\测试\\自动化项目\\flexsafe-1.9.5\\run\\report\\"
report_FileName = u"D:\\Code\\Github\\Lukas_proj\\测试\\自动化项目\\flexsafe-1.9.5\\run\\report\\" + now + 'result.html'

#para
host = "172.16.71.182"
base_url = "http://{host}:8080/#!/login".format(host=host)
#浏览器类型
browser_type = "chrome"
def browser_select():
    if browser_type == "Firefox" or browser_type == "firefox":
        return  webdriver.Firefox()
    elif browser_type == "Chrome" or browser_type == "chrome":
        return webdriver.Chrome()