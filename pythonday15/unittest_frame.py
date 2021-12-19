'''
@File:unittest_frame.py
@DateTime:2021/12/14 22:53
@Author:xiaodong
@Desc:
'''

#test Fixture  #搭建测试的环境
import unittest

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")

    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")

    def setUp(self):
        print("登录禅道")

    def tearDown(self):
        '''成功登录'''
        print("登出禅道")

    def test_adduser(self):
        print("添加组织用户用例")

    def test_showuser(self):
        print("查看组织用户用例")

    def test_updateuser(self):
        print("修改组织用户用例")

    def test_deleteuser(self):
        print("删除组织用户用例")

# if __name__=="__main__":
    # unittest.main()
    s=unittest.TestSuite()
    s.addTest(TestCases("test_adduser"))
    s.addTest(TestCases("test_showuser"))
    s.addTest(TestCases("test_updateuser"))
    s.addTest(TestCases("test_deleteuser"))
    runner=unittest.TextTestRunner()
    runner.run(s)