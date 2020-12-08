import time
import unittest
from BeautifulReport import BeautifulReport

discover = unittest.defaultTestLoader.discover("../test_case",pattern='Recovery_app**.py')


nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
filename = 'Recovery测试报告'+ str(nowtime)
BeautifulReport(discover).report(description='故障自愈接口测试',filename=filename,log_path="../reports")