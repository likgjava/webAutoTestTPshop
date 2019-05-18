import logging
import time
import unittest

from script.test_cart import TestCart
from script.test_login import TestLogin
from script.test_order import TestOrder
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

try:
    DriverUtil.set_auto_quit(False)

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLogin))
    suite.addTest(unittest.makeSuite(TestCart))
    suite.addTest(unittest.makeSuite(TestOrder))

    report_file = "./report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
    with open(report_file, "wb") as f:
        runner = HTMLTestRunner(f, title="TPshop自动化测试报告", description="Win10.Firefox")
        runner.run(suite)
except Exception as e:
    logging.exception(e)
finally:
    DriverUtil.set_auto_quit(True)
    DriverUtil.quit_driver()
