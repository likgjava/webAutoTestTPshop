import json
import sys
import unittest
import logging

from parameterized import parameterized

import utils
from page.home_page import HomeProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


def load_data():
    """
    加载登录测试数据
    """
    test_data = []
    with open(utils.get_data_path() + "login.json", encoding="utf-8") as f:
        json_data = json.load(f)
        for login_data in json_data.values():
            test_data.append((login_data.get("username"),
                              login_data.get("password"),
                              login_data.get("code"),
                              login_data.get("expect")))
    print("test_data=", test_data)
    return test_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_proxy = LoginProxy()
        cls.index_proxy = IndexProxy()
        cls.home_proxy = HomeProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        # 进入登录页面
        self.index_proxy.to_login_page()

    # 登录
    @parameterized.expand(load_data)
    def test_login(self, username, password, code, expect):
        logging.info('username={} password={} code={} expect={}'.
                     format(username, password, code, expect))
        try:
            # 登录
            self.login_proxy.login(username, password, code)

            self.assertTrue(False)

            # 登录成功
            if "登录成功" == expect:
                # 判断是否为‘我的商城’页面
                is_home_page = self.home_proxy.is_home_page()
                self.assertTrue(is_home_page)
        except Exception as e:
            utils.screenshot(self)
            logging.exception(e)
            raise
