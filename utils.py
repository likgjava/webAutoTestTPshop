import os

from selenium import webdriver


def get_data_path():
    """
    获取数据文件所在路径
    :return: 数据文件的绝对路径
    """
    path = os.path.dirname(os.path.abspath(__file__)) + "/data/"
    print("path=", path)
    return path


def get_tips_msg():
    """
    获取弹出框的提示消息
    :return: 消息文本内容
    """
    msg = DriverUtil.get_driver().find_element_by_class_name("layui-layer-content").text
    return msg


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
            DriverUtil._driver = webdriver.Firefox()
            DriverUtil._driver.maximize_window()
            DriverUtil._driver.implicitly_wait(10)
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



