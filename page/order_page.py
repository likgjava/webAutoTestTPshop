from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderPage(BasePage):
    """
    下订单页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 提交订单
        self.submit_order = (By.LINK_TEXT, "提交订单")

    def find_submit_order(self):
        return self.find_element(self.submit_order)


class OrderHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.cart_page = OrderPage()

    def click_submit_order(self):
        self.cart_page.find_submit_order().click()


class OrderProxy:
    """
    业务层
    """

    def __init__(self):
        self.cart_handle = OrderHandle()

    # 提交订单
    def submit_order(self):
        self.cart_handle.click_submit_order()
