#日志简单封装
import os
import logging

current_path = os.path.dirname(__file__)  # 获取当前路径
log_path = os.path.join(current_path, '../logs/test.log')  #路径可以放到配置文件里

class LogUtils:
    def __init__(self, logfile_path=log_path):  # 默认路径
        self.logfile_path = logfile_path  #
        self.logger = logging.getLogger('Logger')  # 创建日志对象
        self.logger.setLevel(level=logging.INFO)  # 全局默认级别
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log = logging.FileHandler(self.logfile_path,encoding='utf-8')  # 文件输出
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

logger = LogUtils()

if __name__ == '__main__':
    log_utils = LogUtils()
    log_utils.info('newdream')

