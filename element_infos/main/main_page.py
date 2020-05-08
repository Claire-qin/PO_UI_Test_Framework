#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: main_page.py
# @time:2020/5/8 12:39 

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

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 登录元素信息 方式一： 读取excel文件
        elments = ElementDataUtil(os.path.dirname(__file__) + cfg.excel_path).get_element_info_dic_by_excel('main', 'nav_bar')
        print(elments)
        self.companyname_showbox = elments['companyname_showbox']
        self.myzone_menu = elments['myzone_menu']
        self.product_menu = elments['product_menu']
        self.project_menu = elments['project_menu']
        self.organization_menu = elments['organization_menu']
        self.username_showspan = elments['username_showspan']

    def get_companyname(self):  # 获取公司名称
        self.get_attribute_title(self.companyname_showbox)

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_menu)
        self.wait(1)

    def goto_product(self):  # 进入产品菜单
        self.click(self.product_menu)
        self.wait(1)

    def goto_project(self):  # 进入项目菜单
        self.click(self.project_menu)
        self.wait(1)

    def goto_organization(self):
        self.click(self.organization_menu)
        self.wait(1)

    def get_username(self):  #
        self.get_text(self.username_showspan)


if __name__ == "__main__":
    driver = Browser().get_driver()
    # 登录
    login_page =  LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/user-login.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
    login_page.wait(2)

    # 主页操作
    main_page = MainPage(login_page.driver)
    main_page.goto_myzone()
    main_page.goto_product()
    main_page.goto_project()
    main_page.goto_organization()



