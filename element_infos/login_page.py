# pageobject设计模块：把页面设计成一个类，页面中的控件作为属性，控件的操作作为方法。
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username_inputbox ={'element_name':'用户名输入框',
                                 'locator_type':'xpath',
                                 'locator_value':'//input[@name="account"]',
                                 'timeout':5}
        self.password__inputbox ={'element_name':'密码输入框',
                                 'locator_type':'xpath',
                                 'locator_value':'//input[@name="password"]',
                                 'timeout':4}
        self.login_button ={'element_name':'登录按钮',
                                 'locator_type':'xpath',
                                 'locator_value':'//button[@id="submit"]',
                                 'timeout':2}

    def input_username(self,username): #方法：操作
        self.input(self.username_inputbox,username)

    def input_password(self,password):
        self.input(self.password__inputbox,password)

    def click_login(self):
        self.click(self.login_button)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/user-login.html')
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()


