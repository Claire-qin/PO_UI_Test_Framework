import os,time
from selenium import webdriver
from common.element_excel_utils import ElementExcelUtil
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from element_infos.organization_page import OrganizationPage

class EditCompanyPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #编辑公司页面 元素信息
        elements = ElementExcelUtil('edit_company_page').get_elemnet_info()
        self.edit_company = elements['edit_company']
        self.company_name_iuputbox = elements['company_name_iuputbox']
        self.save_button = elements['save_button']

    # 进入编辑公司信息 页面
    def goto_edit_company_page(self):
        self.click(self.edit_company)
        time.sleep(1)

    def input_company_name(self,company_name):
        self.input(self.company_name_iuputbox,company_name)

    def click_save(self):
        self.click(self.save_button)

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
    # 进入公司信息页面
    organization = OrganizationPage(driver)
    organization.goto_company()
    # 进入编辑公司信息 页面
    editcompany = EditCompanyPage(driver)
    editcompany.goto_edit_company_page()
    editcompany.input_company_name('无忧')
    editcompany.click_save()