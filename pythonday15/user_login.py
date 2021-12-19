'''
@File:user_login.py
@DateTime:2021/12/14 23:30
@Author:xiaodong
@Desc:
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import unittest

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #打开浏览器
        s = Service(executable_path=r"D:\PythonProject\web_selenium\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()

    # @classmethod
    # def tearDownClass(cls):
        #关闭浏览器
        time.sleep(2)
        cls.driver.quit()
    def setUp(self):
        print("测试开始")

    def test_login(self):
        #登录禅道
        self.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
        self.driver.find_element(By.CSS_SELECTOR,"#account").send_keys("shelly")  # CSS_SELECTOR方式，选择id=#的方式找元素
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("p@ssw0rd")  # XPATH相对路径找元素
        self.driver.find_element(By.CSS_SELECTOR,".form-actions :nth-child(1)").click()  # CSS_SELECTOR方式,选择form-actions作为父元素的第一个子标签元素
        try:
            assert self.driver.title == "我的地盘 - 禅道"
            print("验证登录成功测试----passed")
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME,"user-name").click()
            time.sleep(2)
            self.driver.find_element(By.LINK_TEXT,"退出").click()
        except:
            print("验证登录成功测试----failed")

    def test_loginfalse(self):
        self.driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
        self.driver.find_element(By.CSS_SELECTOR,"#account").send_keys("shelly333")  # CSS_SELECTOR方式，选择id=#的方式找元素
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("12345")  # XPATH相对路径找元素
        self.driver.find_element(By.CSS_SELECTOR,".form-actions :nth-child(1)").click()  # CSS_SELECTOR方式,选择form-actions作为父元素的第一个子标签元素
        try:
            assert self.driver.title == "我的地盘 - 禅道"
            print("验证登录成功测试----passed")
        except:
            print("验证登录成功测试----failed")


    def tearDown(self):
        print("测试结束")

if __name__=="__main__":
    unittest.main()
    # s=unittest.TestSuite()
    # s.addTest(TestCases("test_adduser"))
    # s.addTest(TestCases("test_showuser"))
    # s.addTest(TestCases("test_updateuser"))
    # s.addTest(TestCases("test_deleteuser"))
    # runner=unittest.TextTestRunner()
    # runner.run(s)