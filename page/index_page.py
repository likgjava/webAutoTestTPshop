from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class IndexPage(BasePage):
    """
    对象库层
    """

    def __init__(self):
        super().__init__()

        # 搜索框
        self.search_input = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CSS_SELECTOR, "[type='submit']")
        # 我的购物车
        self.my_cart = (By.ID, "hd-my-cart")
        # 登录链接
        self.login_link = (By.LINK_TEXT, "登录")

    def find_search_input(self):
        return self.find_element(self.search_input)

    def find_search_btn(self):
        return self.find_element(self.search_btn)

    def find_my_cart(self):
        return self.find_element(self.my_cart)

    def find_login_link(self):
        return self.find_element(self.login_link)


class IndexHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.index_page = IndexPage()

    def input_search_kw(self, kw):
        self.input_text(self.index_page.find_search_input(), kw)

    def click_search_btn(self):
        self.index_page.find_search_btn().click()

    def click_my_cart(self):
        self.index_page.find_my_cart().click()

    def click_login_link(self):
        self.index_page.find_login_link().click()


class IndexProxy:
    """
    业务层
    """

    def __init__(self):
        self.index_handle = IndexHandle()

    # 搜索关键字
    def search_kw(self, kw):
        # 输入关键字
        self.index_handle.input_search_kw(kw)
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