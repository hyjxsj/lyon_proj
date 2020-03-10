#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

from selenium import webdriver
import unittest,time,sys

class test_SubModule1(unittest.TestCase):
    def setUp(self):
        '''
        模板如下：
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)   #这个版本的driver和python版本不生效
        self.base_url = "http://www.baidu.com"
        '''
        pass
    def test_case1(self):
        '''
        具体的测试用例在这写，模板如下：
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")
        '''
        submodule_name = self.__class__.__name__
        case_name = sys._getframe().f_code.co_name
        print('\n'+"--------------->%s测试开始" % (submodule_name+'.'+case_name))
        print("当前子模块名：%s" % submodule_name)
        print("当前用例名：%s" % case_name)
    def test_case2(self):
        submodule_name = self.__class__.__name__
        case_name = sys._getframe().f_code.co_name
        print('\n'+"--------------->%s测试开始" % (submodule_name+'.'+case_name))
        print("当前子模块名：%s" % submodule_name)
        print("当前用例名：%s" % case_name)
    def tearDown(self):
        '''
        #模板，执行完测试用例后处理
        self.driver.quit()
        '''
        pass

if __name__ == "__main__":
    '''
    # unittest.main()  #直接调用unittest封装的main方法，执行用例顺序是按照用例名ASCII码排序
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_case'))
    suite.addTest(MyTest('test_case2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)   
    '''
    suite = unittest.TestSuite()
    suite.addTest(test_SubModule1('test_case1'))
    suite.addTest(test_SubModule1('test_case2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)


