from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderPayPage(BasePage):
    """
    订单支付-对象库层
    """

    def __init__(self):
        super().__init__()

        # 货到付款
        self.cod = (By.CSS_SELECTOR, "input[value='pay_code=cod']")
        # 确认支付方式
        self.confirm_pay = (By.LINK_TEXT, "确认支付方式")

    def find_cod(self):
        return self.find_element(self.cod)

    def find_confirm_pay(self):
        return self.find_element(self.confirm_pay)


class OrderPayHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.cart_page = OrderPayPage()

    def click_cod(self):
        self.cart_page.find_cod().click()

    def click_confirm_pay(self):
        self.cart_page.find_confirm_pay().click()


class OrderPayProxy:
    """
    业务层
    """

    def __init__(self):
        self.cart_handle = OrderPayHandle()

    # 确认支付
    def confirm_pay(self):
        self.cart_handle.click_cod()
        self.cart_handle.click_confirm_pay()
