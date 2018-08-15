import logging.handlers

# 日志输出格式
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(fmt)

# 输出到控制台
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

# 输出到文件
# fh = logging.FileHandler("./log/tpshop.log")
# fh.setFormatter(formatter)
# logger.addHandler(fh)

# 输出到文件，每日一个文件
fh = logging.handlers.TimedRotatingFileHandler("log/tpshop.log", when='D', interval=1, backupCount=3)
fh.setFormatter(formatter)
logger.addHandler(fh)

logging.info("hello")
logging.error("error")
