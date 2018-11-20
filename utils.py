import logging
import os
import time

from selenium import webdriver


def get_data_path():
    """
    获取数据文件所在路径
    :return: 数据文件的绝对路径
    """
    path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    print("path=", path)
    return path


def get_screenshot_path():
    """
    获取保存截图所在路径
    :return: 存放截图的绝对路径
    """
    path = os.path.dirname(os.path.abspath(__file__)) + "/screenshot/"
    print("screenshot=", path)
    return path


def screenshot(case):
    """"""
    t = time.strftime("%Y%m%d-%H%M%S")
    img_path = get_screenshot_path() + "{}-{}.png".format(case._testMethodName, t)
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
    except Exception:
        print("current page not contains [{}]".format(text))
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

    @staticmethod
    def get_driver():
        """
        获取浏览器驱动对象，并完成初始化设置
        :return: 浏览器驱动对象
        """
        if DriverUtil._driver is None:
            logging.info("init driver...")
            DriverUtil._driver = webdriver.Firefox()
            DriverUtil._driver.maximize_window()
            DriverUtil._driver.implicitly_wait(20)
            DriverUtil._driver.get("http://localhost")
        return DriverUtil._driver

    @staticmethod
    def quit_driver():
        """
        关闭浏览器驱动
        """
        if DriverUtil._auto_quit:
            DriverUtil.get_driver().quit()

    @staticmethod
    def set_auto_quit(auto_quit):
        """
        设置测试类运行完毕后，是否自动关闭驱动对象
        """
        DriverUtil._auto_quit = auto_quit
