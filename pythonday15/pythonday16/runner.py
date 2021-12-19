'''
@File:runner.py
@DateTime:2021/12/17 17:47
@Author:xiaodong
@Desc:
'''
import unittest
from BeautifulReport import BeautifulReport

cases=unittest.defaultTestLoader.discover(start_dir=r"D:\PythonProject\dxd\Python\pythonday15\pythonday16",pattern='test*.py')
result=BeautifulReport(cases)
result.report(description="系统用户的测试报告",filename="登录模块测试报告",report_dir=r"D:\PythonProject\dxd\Python\pythonday15\pythonday16\report")