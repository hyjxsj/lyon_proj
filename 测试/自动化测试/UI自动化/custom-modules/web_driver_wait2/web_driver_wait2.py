#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverWait2(object):
    def __init__(self,driver,ele_by_xpath=None):
        self.dr = driver
        self.ele_by_xpath = ele_by_xpath

    def explicitly(self,timeout):
        ele = WebDriverWait(self.dr, timeout).until(EC.presence_of_element_located((By.XPATH, self.ele_by_xpath)))
        return ele
    def implicitly(self,timeout):
        self.dr.implicitly_wait(timeout)
