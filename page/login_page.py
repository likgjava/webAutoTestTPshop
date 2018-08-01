from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """
    对象库层
    """

    def __init__(self):
        super().__init__()

        # 用户名输入框
        self.username = (By.ID, "username")
        # 密码
        self.password = (By.ID, "password")
        # 验证码
        self.verify_code = (By.ID, "verify_code")
        # 登录按钮
        self.login_btn = (By.NAME, "sbtbutton")

    def find_username(self):
        return self.find_element(self.username)

    def find_password(self):
        return self.find_element(self.password)

    def find_verify_code(self):
        return self.find_element(self.verify_code)

    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, pwd):
        self.input_text(self.login_page.find_password(), pwd)

    def input_verify_code(self, code):
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:
    """
    业务层
    """

    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录
    def login(self, username, password, verify_code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 输入验证码
        self.login_handle.input_verify_code(verify_code)
        # 点击登录按钮
        self.login_handle.click_login_btn()

