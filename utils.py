import logging
import time

from selenium import webdriver

import config


def screenshot(case):
    """"""
    t = time.strftime("%Y%m%d-%H%M%S")
    img_path = config.BASE_DIR + "/screenshot/{}-{}.png".format(case._testMethodName, t)
    DriverUtil.get_driver().get_screenshot_as_file(img_path)


def get_tips_msg():
    """
    获取弹出框的提示消息
    :return: 消息文本内容
    """
    msg = DriverUtil.get_driver().find_element_by_class_name("layui-layer-content").text
    return msg


def exist_text(text):
    """
    判断页面中是否存在指定的文本内容
    :param text: 文本内容
    :return: True:存在; False:不存在
    """
    try:
        xpath = "//*[contains(text(), '{}')]".format(text)
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element is not None
    except Exception as e:
        print("current page not contains [{}]".format(text))
        logging.exception(e)
        return False


def switch_new_window():
    """
    切换到新窗口
    """
    # 等待一下新窗口的打开
    time.sleep(3)
    driver = DriverUtil.get_driver()
    driver.switch_to.window(driver.window_handles[-1])


class DriverUtil:
    """
    浏览器驱动工具类
    """
    _driver = None
    _auto_quit = True

    @classmethod
    def get_driver(cls):
        """
        获取浏览器驱动对象，并完成初始化设置
        :return: 浏览器驱动对象
        """
        if cls._driver is None:
            logging.info("init driver...")
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get("http://localhost")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """
        关闭浏览器驱动
        """
        if cls._auto_quit and cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def set_auto_quit(cls, auto_quit):
        """设置是否自动退出驱动"""
        cls._auto_quit = auto_quit
