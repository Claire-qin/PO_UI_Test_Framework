#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: login_action.py
# @time:2020/5/12 21:18 
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_util import cfg

class LoginAction:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self,username,password):
        self.login_action(username,password)
        return MainPage(self.login_page.driver)

    def default_login(self):
        return self.login_success(cfg.user_name,cfg.password)

    def login_fail(self,username,password):

        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    def login_by_cookie(self):
        pass
