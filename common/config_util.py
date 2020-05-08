#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: element_data_util.py
# @time:2020/5/8 10:49

import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir, "..", 'conf',"config.ini")

class ConfigUtil(object):
    def __init__(self,path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path,encoding='utf-8')

    @property
    def url(self):
        url_value = self.cfg.get('default','url')
        return url_value

    @property
    def driver_path(self):
        driver_path_value = self.cfg.get('default','driver_path')
        return driver_path_value

    @property
    def driver_name(self):
        driver_name_value = self.cfg.get('default', 'driver_name')
        return driver_name_value

    @property
    def time_out(self):
        driver_name_value = float(self.cfg.get('default', 'time_out'))
        return driver_name_value

    @property
    def screenshot_path(self):
        screenshot_path_value = self.cfg.get('default', 'screen_shot_path')
        return screenshot_path_value

    @property
    def log_path(self):
        log_path_value = self.cfg.get('default', 'log_path')
        return log_path_value

    @property
    def log_level(self):
        log_level_value = int(self.cfg.get('default', 'log_level'))
        return log_level_value

    @property
    def user_name(self):
        user_name_value = self.cfg.get('default', 'user_name')
        return user_name_value

    @property
    def password(self):
        password_value = self.cfg.get('default', 'password')
        return password_value

    @property
    def excel_path(self):
        excel_path_value = self.cfg.get('default', 'excel_path')
        return excel_path_value


cfg = ConfigUtil()

if __name__=='__main__':
    config = ConfigUtil()
    print(config.user_name)
    print(config.password)
    print(config.log_level)