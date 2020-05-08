#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: first_page.py.py
# @time:2020/5/8 12:35

import os
from common.base_page import BasePage
from common.element_data_util import ElementDataUtil
from common.browser import Browser
from common.config_util import cfg
from element_infos.login.login_page import LoginPage

class FirstPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 登录元素信息 方式一： 读取excel文件
        elments = ElementDataUtil(os.path.dirname(__file__) + cfg.excel_path).get_element_info_dic_by_excel('myzone', 'first_page')

        self.home = elments['home']
        self.calendar = elments['calendar']
        self.task = elments['task']
        self.bug = elments['bug']
        self.test_task = elments['test_task']
        self.my_story = elments['my_story']
        self.my_project = elments['my_project']
        self.my_dynamic = elments['my_dynamic']
        self.my_profile = elments['my_profile']
        self.my_change_pwd = elments['my_change_pwd']
        self.my_contacts = elments['my_contacts']

    def goto_home(self):
        self.click(self.home)
        self.wait(1)

    def goto_calendar(self):
        self.click(self.calendar)
        self.wait(1)

    def goto_task(self):
        self.click(self.task)
        self.wait(1)

    def goto_bug(self):
        self.click(self.bug)
        self.wait(1)

if __name__ == "__main__":
    driver = Browser().get_driver()
    login_page =  LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/user-login.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
    login_page.wait(2)

    first_page =FirstPage(login_page.driver)
    first_page.goto_calendar()
    first_page.goto_task()
    first_page.goto_bug()
    first_page.goto_home()