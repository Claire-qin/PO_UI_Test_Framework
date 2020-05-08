#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: element_data_util.py
# @time:2020/5/8 10:49

import os
import logging
import time
from common.config_util import cfg

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '..', cfg.log_path)

class LogUtil(object):
    def __init__(self,logger=None):
        self.log_name = os.path.join(log_path, 'UITest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(cfg.log_level) #

        self.fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        self.fh.setLevel(cfg.log_level)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(cfg.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger

logger = LogUtil().get_log()

if __name__=='__main__':
    logger.info( 'test_info_log' )
    logger.error('test_error_log')