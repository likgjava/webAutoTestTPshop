from selenium.webdriver.common.by import By

import utils
from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()

        # 登录链接
        self.login_link = (By.LINK_TEXT, "登录")
        # 搜索框
        self.search = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CSS_SELECTOR, "[type='submit']")
        # 我的购物车
        self.my_cart = (By.ID, "hd-my-cart")
        # 我的订单链接
        self.my_order_link = (By.LINK_TEXT, "我的订单")

    def find_login_link(self):
        return self.find_element(self.login_link)

    def find_search(self):
        return self.find_element(self.search)

    def find_search_btn(self):
        return self.find_element(self.search_btn)

    def find_my_cart(self):
        return self.find_element(self.my_cart)

    def find_my_order_link(self):
        return self.find_element(self.my_order_link)


class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()

    def click_login_link(self):
        self.index_page.find_login_link().click()

    def input_search(self, goods_name):
        self.input_text(self.index_page.find_search(), goods_name)

    def click_search_btn(self):
        self.index_page.find_search_btn().click()

    def click_my_cart(self):
        self.index_page.find_my_cart().click()

    def click_my_order_link(self):
        self.index_page.find_my_order_link().click()


class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 搜索商品
    def search_goods(self, goods_name):
        # 输入商品名称
        self.index_handle.input_search(goods_name)
        # 点击搜索按钮
        self.index_handle.click_search_btn()

    # 进入登录页面
    def to_login_page(self):
        # 点击登录链接
        self.index_handle.click_login_link()

    # 进入购物车页面
    def to_cart_page(self):
        # 点击'我的购物车'
        self.index_handle.click_my_cart()

    # 进入首页
    def to_index_page(self):
        DriverUtil.get_driver().get("http://localhost")

    # 进入我的订单页面
    def to_my_order_page(self):
        self.index_handle.click_my_order_link()

        # 切换到新窗口
        utils.switch_new_window()
