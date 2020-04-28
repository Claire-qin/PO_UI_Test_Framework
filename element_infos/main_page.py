import os
import time
from selenium import webdriver
from element_infos.login_page import LoginPage
from common.base_page import BasePage
from common.element_excel_utils import ElementExcelUtil

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 主页面元素信息
        elments = ElementExcelUtil('main_page').get_elemnet_info()
        self.companyname_showbox  = elments['companyname_showbox']
        self.myzone_menu = elments['myzone_menu']
        self.product_menu = elments['product_menu']
        self.project_menu = elments['project_menu']
        self.organization_menu = elments['organization_menu']
        self.username_showspan = elments['username_showspan']

    # self.companyname_showbox = self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
    def get_companyname(self):  # 获取公司名称
        self.get_attribute_title(self.companyname_showbox)

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_menu)
        time.sleep(1)

    def goto_product(self):  # 进入产品菜单
        self.click(self.product_menu)
        time.sleep(1)

    def goto_project(self):  # 进入项目菜单
        self.click(self.project_menu)
        time.sleep(1)

    def goto_organization(self):
        self.click(self.organization_menu)
        time.sleep(1)

    def get_username(self):  #
        self.get_text(self.username_showspan)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    # 登录
    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/my')
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
    # 主页面
    main_page = MainPage(driver)
    main_page.get_companyname()
    main_page.goto_myzone()
    main_page.goto_product()
    main_page.goto_project()
    main_page.goto_organization()
    main_page.get_username()