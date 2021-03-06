from utils import DriverUtil
import logging


class BasePage:
    """
    对象库层-基类
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        logging.info("location={}".format(location))
        return self.driver.find_element(location[0], location[1])


class BaseHandle:
    """
    操作层-基类
    """

    def input_text(self, element, text):
        """
        在输入框里输入文本内容，先清空再输入
        :param element: 要操作的元素
        :param text: 要输入的文本内容
        """
        element.clear()
        element.send_keys(text)
