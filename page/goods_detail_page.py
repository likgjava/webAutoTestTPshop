from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    """
    商品详情页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 加入购物车
        self.join_cart = (By.ID, "join_cart")
        # 添加结果
        self.join_result = (By.CSS_SELECTOR, "div.conect-title>span")

    def find_join_cart(self):
        return self.find_element(self.join_cart)

    def find_join_result(self):
        return self.find_element(self.join_result)


class GoodsDetailHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_join_cart(self):
        self.goods_detail_page.find_join_cart().click()

    def get_join_result(self):
        return self.goods_detail_page.find_join_result().text


class GoodsDetailProxy:
    """
    业务层
    """

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    # 把商品添加到购物车
    def join_cart(self):
        # 点击加入购物车
        self.goods_detail_handle.click_join_cart()

    def is_join_success(self):
        frame = DriverUtil.get_driver().find_element_by_tag_name("iframe")
        DriverUtil.get_driver().switch_to.frame(frame)
        join_result = self.goods_detail_handle.get_join_result()
        return "添加成功" in join_result

