import os
import time
from selenium import webdriver
from common.element_excel_utils import ElementExcelUtil
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from element_infos.organization_page import OrganizationPage

class DeleteDepts(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 项目管理 页面元素
        elements = ElementExcelUtil('delete_depts_page').get_elemnet_info()
        self.delete = elements['delete']

    def accept_delete(self):
        self.clik_confirm_delete(self.delete)

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
    # 进入部门信息页面
    organization = OrganizationPage(driver)
    organization.goto_depts()
    # 删除部门
    delete_depts = DeleteDepts(driver)
    delete_depts.accept_delete()