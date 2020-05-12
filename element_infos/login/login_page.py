#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: pogin_page.py
# @time:2020/5/8 11:49
# pageobject设计模块：把页面设计成一个类，页面中的控件作为属性，控件的操作作为方法。

import os
from common.base_page import BasePage
from common.element_data_util import ElementDataUtil
from common.browser import Browser
from common.config_util import cfg

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 登录元素信息 方式一： 读取excel文件
        elments = ElementDataUtil(os.path.dirname(__file__) + cfg.excel_path).get_element_info_dic_by_excel('login', 'login_page')

        # 登录元素信息 方式二： 读取yaml文件
        # elments = ElementDataUtil(os.path.dirname(__file__) + '/../../element_infos_datas/login_page.yaml').get_element_info_dic_by_yaml()

        self.username_inputbox = elments['username_inputbox']
        self.password_inputbox = elments['password_inputbox']
        self.login_button = elments['login_button']

    def input_username(self, username):
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

    def get_login_fail_alert_content(self):
        return self.switch_to_alert()

if __name__ == "__main__":
    driver = Browser().get_driver()
    login_page =  LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/user-login.html')
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
    login_page.wait(2)
    login_page.screenshot_as_file()



