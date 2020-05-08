#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: add_product_page.py
# @time:2020/5/8 12:21 

import os
from common.base_page import BasePage
from common.element_data_util import ElementDataUtil
from common.browser import Browser
from common.config_util import cfg
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
class AddProductPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 获取元素信息
        elments = ElementDataUtil(os.path.dirname(__file__) + cfg.excel_path).get_element_info_dic_by_excel('product', 'add_product_page')
        self.product_create_button  = elments['product_create_button']
        self.product_title_inputbox = elments['product_title_inputbox']
        self.product_code_inputbox = elments['product_code_inputbox']
        self.line_chosen_popup = elments['line_chosen_popup']  # 弹窗
        self.line_chosen = elments['line_chosen']
        self.po_chosen_popup = elments['po_chosen_popup']
        self.po_chosen = elments['po_chosen']
        self.qd_chosen_popup = elments['qd_chosen_popup']
        self.qd_chosen = elments['qd_chosen']
        self.rd_chosen_popup = elments['rd_chosen_popup']
        self.rd_chosen = elments['rd_chosen']
        self.type_select = elments['type_select']
        self.product_description_inputbox = elments['product_description_inputbox']
        self.access_control_chosen = elments['access_control_chosen']
        self.save_button = elments['save_button']
        self.iframe = elments['iframe']

    def goto_add_product(self):
        self.click(self.product_create_button)

    def input_product_title(self,title):
        self.input(self.product_title_inputbox,title)

    def input_product_code(self,code):
        self.input(self.product_code_inputbox,code)

    def choose_product_line(self):
        self.click(self.line_chosen_popup)
        self.click(self.line_chosen)

    def choose_po_chosen(self):
        self.click(self.po_chosen_popup)
        self.click(self.po_chosen)

    def choose_qd_chosen(self):
        self.click(self.qd_chosen_popup)
        self.click(self.qd_chosen)

    def choose_rd_chosen(self):
        self.click(self.rd_chosen_popup)
        self.click(self.rd_chosen)

    def select_product_type(self,value):  # 产品类型下拉选择
        self.select_value(self.type_select,value)

    def input_product_description(self,description):
        self.input(self.product_description_inputbox,description)

    def radio_access_control(self):  # 访问控制选择
        self.click(self.access_control_chosen)

    def switch_to_iframe(self):
        self.switch_to_frame(self.iframe)

    def switch_to_default_content(self):
        self.driver.switch_to_default_content()

    def click_save(self):
        self.click(self.save_button)

if __name__ == '__main__':
    driver = Browser().get_driver()
    # 登录
    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/user-login.html')
    login_page.set_browser_max()
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
    login_page.wait(2)

    # 主页
    main_page = MainPage(driver)
    main_page.goto_product()

    # 添加产品页面
    add_product_page = AddProductPage(driver)
    add_product_page.goto_add_product()
    add_product_page.input_product_title('产品05')
    add_product_page.input_product_code('product05')
    add_product_page.choose_product_line()
    add_product_page.choose_po_chosen()
    add_product_page.choose_qd_chosen()
    add_product_page.choose_rd_chosen()
    add_product_page.select_product_type('branch')  # branch：多分支(适用于客户定制场景)，normal：正常

    # 进入iframe
    add_product_page.switch_to_iframe()
    add_product_page.input_product_description('这里是产品描述信息')
    add_product_page.switch_to_default_content()
    add_product_page.radio_access_control()
    add_product_page.click_save()



