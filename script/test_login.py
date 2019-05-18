import json
import logging
import time
import unittest

from parameterized import parameterized

import config
import utils
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


# 加载登录测试数据
def load_data():
    test_data = []
    with open(config.BASE_DIR + "/data/login.json", encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            test_data.append((case_data.get("username"),
                              case_data.get("password"),
                              case_data.get("code"),
                              case_data.get("expect")))
    logging.info("test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        # 进入登录页面
        self.index_proxy.to_login_page()

    @parameterized.expand(load_data)
    def test_login(self, username, password, code, expect):
        """登录"""
        logging.info('username={} password={} code={} expect={}'.format(username, password, code, expect))
        print("test_login start...")
        try:
            # 登录
            self.login_proxy.login(username, password, code)

            # 断言
            time.sleep(3)
            self.assertIn(expect, self.driver.title)
        except Exception as e:
            utils.screenshot(self)
            logging.exception(e)
            raise
