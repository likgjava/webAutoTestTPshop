import unittest

from page.home_page import HomeProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


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
    def test_login(self):
        # 登录
        self.login_proxy.login("13012345678", "123456", "8888")

        # 判断是否为‘我的商城’页面
        is_home_page = self.home_proxy.is_home_page()

        self.assertTrue(is_home_page)
