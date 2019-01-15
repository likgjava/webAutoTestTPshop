import logging.handlers
import os

# 工程目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)


def init_log_config():
    """
    初始化日志配置
    """

    # 日志输出格式
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt)

    # 输出到控制台
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # 输出到文件，每日一个文件
    log_path = os.path.join(BASE_DIR, "log", "tpshop.log")
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when='MIDNIGHT', interval=1, backupCount=3)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# 初始化日志配置
# init_log_config()

# logging.info("hello")
# logging.error("error")
