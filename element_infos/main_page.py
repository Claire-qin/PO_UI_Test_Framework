# pageobject设计模块：把页面设计成一个类，页面中的控件作为属性，控件的操作作为方法。
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log_utils import logger

class MainPage:
    def __init__(self):
        login_page = LoginPage()
        login_page.input_username('admin')
        login_page.input_password('admin123456')
        login_page.click_login()
        self.driver = login_page.driver #识别元素要drirver

        self.companyname_showbox = self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.myzone_menu = self.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.product_menu = self.driver.find_element(By.XPATH, '//li[@data-id="product"]')
        self.username_showspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')

    def get_companyname(self): #获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        return value

    def goto_myzone(self):  #进入我的地盘菜单
        self.myzone_menu.click()

    def goto_product(self): #进入产品菜单
        self.product_menu.click()

    def get_username(self): #
        vavlue = self.username_showspan.text
        logger.info('获取用户名成功，用户名是：：' + str(vavlue))
        return vavlue

if __name__ == "__main__":
    main_page = MainPage()
    username= main_page.get_username()
    print(username)