# 导包
import unittest

from conftest import base_url
from tools.HTMLTestRunner import HTMLTestRunner
# 组装测试套件
suite = unittest.defaultTestLoader.discover(base_url + "/scripts", pattern="test*.py")
# 获取报告存储文件实例化HTMLTestRunner调用run执行测试套件
with open("./report/report.html", "wb") as s:
    HTMLTestRunner(stream=s).run(suite)