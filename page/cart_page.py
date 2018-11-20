from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):
    """
    购物车页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 全选
        self.check_all = (By.CLASS_NAME, "checkCartAll")
        # 删除选中商品
        self.remove_goods = (By.ID, "removeGoods")
        # 空购物车
        self.empty_cart = (By.CLASS_NAME, "shopcar_empty")
        # 去结算
        self.go_balance = (By.LINK_TEXT, "去结算")

    def find_check_all(self):
        return self.find_element(self.check_all)

    def find_remove_goods(self):
        return self.find_element(self.remove_goods)

    def find_empty_cart(self):
        return self.find_element(self.empty_cart)

    def find_go_balance(self):
        return self.find_element(self.go_balance)


class CartHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.cart_page = CartPage()

    def check_all_goods(self):
        if not self.cart_page.find_check_all().is_selected():
            self.cart_page.find_check_all().click()

    def click_remove_goods(self):
        self.cart_page.find_remove_goods().click()

    def is_empty_cart(self):
        return self.cart_page.find_empty_cart().is_displayed()

    def click_go_balance(self):
        self.cart_page.find_go_balance().click()


class CartProxy:
    """
    业务层
    """

    def __init__(self):
        self.cart_handle = CartHandle()

    # 清空购物车
    def clean_cart(self):
        # 全选商品
        self.cart_handle.check_all_goods()
        # 删除
        self.cart_handle.click_remove_goods()

    # 判断购物车是否为空
    def is_empty_cart(self):
        return self.cart_handle.is_empty_cart()

    # 去结算
    def go_balance(self):
        return self.cart_handle.click_go_balance()
