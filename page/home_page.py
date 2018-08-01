from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class HomePage(BasePage):
    """
    对象库层
    """

    def __init__(self):
        super().__init__()

        # 我的商城
        self.my_shop = (By.LINK_TEXT, "我的商城")

    def find_my_shop(self):
        return self.find_element(self.my_shop)


class HomeHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.home_page = HomePage()

    def exist_my_shop(self):
        try:
            return self.home_page.find_my_shop() is not None
        except Exception:
            print("我的商城元素不存在！")
            return False


class HomeProxy:
    """
    业务层
    """

    def __init__(self):
        self.home_handle = HomeHandle()

    # 判断当前页面是否为后台页面
    def is_home_page(self):
        return self.home_handle.exist_my_shop()
