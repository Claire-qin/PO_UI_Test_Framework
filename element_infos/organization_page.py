import os
from selenium import webdriver
from common.element_excel_utils import ElementExcelUtil
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage

class OrganizationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #组织页面 元素信息
        elements = ElementExcelUtil('organization_page').get_elemnet_info()
        self.company = elements['company']
        self.browse_user = elements['browse_user']
        self.depts =elements['depts']

    # 进入用户 页面
    def goto_browse_user(self):
        self.click(self.browse_user)
    # 进入部门页面
    def goto_depts(self):
        self.click(self.depts)
    # 进入公司信息 页面
    def goto_company(self):
        self.click(self.company)

if __name__ == '__main__':
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
    # 进入组织
    main_page = MainPage(driver)
    main_page.goto_organization()
    # 进入组织各页面
    organization = OrganizationPage(driver)
    organization.goto_browse_user()
    organization.goto_depts()
    organization.goto_company()