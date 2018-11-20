from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MyOrderPage(BasePage):
    """
    我的订单-对象库层
    """

    def __init__(self):
        super().__init__()

        # 待付款
        self.wait_pay_link = (By.LINK_TEXT, "待付款")
        # 立即支付
        self.now_pay_link = (By.LINK_TEXT, "立即支付")

    def find_wait_pay_link(self):
        return self.find_element(self.wait_pay_link)

    def find_now_pay_link(self):
        return self.find_element(self.now_pay_link)


class MyOrderHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.cart_page = MyOrderPage()

    def click_wait_pay_link(self):
        self.cart_page.find_wait_pay_link().click()

    def click_now_pay_link(self):
        self.cart_page.find_now_pay_link().click()


class MyOrderProxy:
    """
    业务层
    """

    def __init__(self):
        self.cart_handle = MyOrderHandle()

    # 去支付
    def go_pay(self):
        self.cart_handle.click_wait_pay_link()
        self.cart_handle.click_now_pay_link()
