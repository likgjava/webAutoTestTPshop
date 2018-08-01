from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class GoodsSearchPage(BasePage):
    """
    商品搜索页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 商品条目
        self.goods_item = (By.XPATH, "//*[@class='shop_name2']/a[contains(text(), '{}')]")

    def find_goods_item(self, goods_name):
        location = (self.goods_item[0], self.goods_item[1].format(goods_name))
        return self.find_element(location)


class GoodsSearchHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.goods_search_page = GoodsSearchPage()

    def click_goods_item(self, goods_name):
        self.goods_search_page.find_goods_item(goods_name).click()


class GoodsSearchProxy:
    """
    业务层
    """

    def __init__(self):
        self.goods_search_handle = GoodsSearchHandle()

    # 跳转到商品详情页
    def to_goods_detail_page(self, goods_name):
        # 点击商品
        self.goods_search_handle.click_goods_item(goods_name)
