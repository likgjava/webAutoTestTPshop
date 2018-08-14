import json
import time
import unittest

from parameterized import parameterized

import utils
from page.cart_page import CartProxy
from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.home_page import HomeProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


def add_goods_to_cart_data():
    """
    添加商品到购物车-测试数据
    """
    test_data = []
    with open(utils.get_data_path() + "cart.json", encoding="utf-8") as f:
        json_data = json.load(f)
        data = json_data.get("test_add_goods_to_cart")
        test_data.append((data.get("goods_name")))
    return test_data


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_proxy = LoginProxy()
        cls.index_proxy = IndexProxy()
        cls.home_proxy = HomeProxy()
        cls.goods_search_proxy = GoodsSearchProxy()
        cls.goods_detail_proxy = GoodsDetailProxy()
        cls.cart_proxy = CartProxy()

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        self.index_proxy.to_index_page()

    # 添加商品到购物车
    @parameterized.expand(add_goods_to_cart_data)
    def test_add_goods_to_cart(self, goods_name):
        # 搜索商品
        self.index_proxy.search_kw(goods_name)

        # 点击商品进入商品详情页
        self.goods_search_proxy.to_goods_detail_page(goods_name)

        # 添加商品到购物车
        self.goods_detail_proxy.join_cart()

        # 判断是否添加成功
        join_success = self.goods_detail_proxy.is_join_success()

        self.assertTrue(join_success)

    # 清空购物车
    def test_clean_cart(self):
        # 进入购物车
        self.index_proxy.to_cart_page()

        # 清空购物车
        self.cart_proxy.clean_cart()

        # 暂停
        time.sleep(3)

        # 判断是否为空
        is_empty = self.cart_proxy.is_empty_cart()

        self.assertTrue(is_empty)

