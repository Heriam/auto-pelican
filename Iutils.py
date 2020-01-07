import os
import sys
import logging
import configparser

# 常量定义 ====
PROJECT_NAME = 'auto-pelican'
DEFAULT_OPTION = 0

# 工具对象 ====
# Python版本
env_python_version = '.'.join(str(i) for i in sys.version_info[:3])

# 绝对路径
env_absolute_path = os.path.abspath(__file__).replace(os.path.basename(__file__),'')

# 初始化日志工具
logger = logging.getLogger(PROJECT_NAME)
logger.setLevel(logging.DEBUG)
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler(filename=env_absolute_path + '%s.log' % PROJECT_NAME, encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

# 读取配置文件
config = configparser.ConfigParser()
config.read('%s.properties' % PROJECT_NAME)


# 工具方法 ====
def info(info):
    print("\n[INFO]%s" % info)

def error(error):
    print("\n[ERROR]%s" % error)