import json
import time
import unittest

from parameterized import parameterized

import config
import utils
from page.cart_page import CartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_page import OrderProxy
from page.order_pay_page import OrderPayProxy
from utils import DriverUtil


def order_data():
    """
    下订单-测试数据
    """
    test_data = []
    with open(config.BASE_DIR + "/data/order.json", encoding="utf-8") as f:
        json_data = json.load(f)
        data = json_data.get("test_order")
        test_data.append((data.get("expect")))
    return test_data


def order_pay_data():
    """
    订单支付-测试数据
    """
    test_data = []
    with open(config.BASE_DIR + "/data/order.json", encoding="utf-8") as f:
        json_data = json.load(f)
        data = json_data.get("test_order_pay")
        test_data.append((data.get("expect")))
    return test_data


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.index_proxy = IndexProxy()
        cls.cart_proxy = CartProxy()
        cls.order_proxy = OrderProxy()
        cls.my_order_proxy = MyOrderProxy()
        cls.order_pay_proxy = OrderPayProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        self.index_proxy.to_index_page()

    # 下订单
    @parameterized.expand(order_data)
    def test01_order(self, expect):
        # 进入购物车页
        self.index_proxy.to_cart_page()

        # 去结算
        self.cart_proxy.go_balance()

        # 等待收货人加载
        time.sleep(3)

        # 提交订单
        self.order_proxy.submit_order()

        # 判断是否提交成功
        submit_success = utils.exist_text(expect)
        self.assertTrue(submit_success)

    # 订单支付
    @parameterized.expand(order_pay_data)
    def test02_order_pay(self, expect):
        # 进入我的订单
        self.index_proxy.to_my_order_page()

        # 立即支付
        self.my_order_proxy.go_pay()

        # 切换到新窗口
        utils.switch_new_window()

        # 确认支付
        self.order_pay_proxy.confirm_pay()

        # 判断是否提交成功
        submit_success = utils.exist_text(expect)
        self.assertTrue(submit_success)
