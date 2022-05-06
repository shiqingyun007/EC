# _*_coding:utf-8_*_
# Author:Teacher shi
# Website:www.hzdledu.com
# Time:2022-04-18 16:13
# Software:PyCharm
# File:run.py
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(r'../testcase', 'test*')  # 创建测试套件

with open(r'../log/reporter%s.html' % time.strftime('%Y-%m-%d %H时%M分%S秒'), mode='wb') as file:
    runner = HTMLTestRunner(file, title="ECMoblie自动化测试报告", description="主流程测试")
    runner.run(suite)
