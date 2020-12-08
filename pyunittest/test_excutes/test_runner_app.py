import time
import unittest
from BeautifulReport import BeautifulReport

discover = unittest.defaultTestLoader.discover("../test_case",pattern='test_case_app**.py')


nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
filename = '测试报告'+ str(nowtime)
BeautifulReport(discover).report(description='APP接口测试',filename=filename,log_path="../reports")