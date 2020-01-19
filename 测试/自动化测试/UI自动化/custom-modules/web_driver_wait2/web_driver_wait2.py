#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverWait2(object):
    def __init__(self,driver,timeout,ele_by_xpath):
        self.dr = driver
        self.timeout = timeout
        self.ele_by_xpath = ele_by_xpath

    def explicitly(self):
        ele = WebDriverWait(self.dr, self.timeout).until(EC.presence_of_element_located((By.XPATH, self.ele_by_xpath)))
        return ele
    def implicitly(self):
        self.dr.implicitly_wait(self.timeout)
