import time
import traceback
import unittest

from script.test_cart import TestCart
from script.test_login import TestLogin

from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

try:
    DriverUtil.set_auto_quit(False)

    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    suite.addTest(TestCart("test_add_goods_to_cart"))
    suite.addTest(TestCart("test_clean_cart"))

    report_file = "./report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
    with open(report_file, "wb") as f:
        runner = HTMLTestRunner(f, title="TPshop商城自动化测试报告", description="Win10.Firefox")
        runner.run(suite)
except Exception as e:
    traceback.print_exc()
finally:
    DriverUtil.set_auto_quit(True)
    DriverUtil.quit_driver()



