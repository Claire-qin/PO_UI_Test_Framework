# pageobject设计模块：把页面设计成一个类，页面中的控件作为属性，控件的操作作为方法。
import os
from selenium import webdriver
from common.base_page import BasePage
from common.element_excel_utils import ElementExcelUtil
from common.element_yaml_util import ElementYamlUtil
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 登录元素信息 读取excel文件
        # elments = ElementExcelUtil('login_page').get_elemnet_info()

        # 登录元素信息 读取yaml文件
        elments = ElementYamlUtil('login_page').get_elemnet_info()

        self.username_inputbox = elments['username_inputbox']
        self.password_inputbox = elments['password_inputbox']
        self.login_button = elments['login_button']

    def input_username(self, username):  # 方法：操作
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)

    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/my')
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()


