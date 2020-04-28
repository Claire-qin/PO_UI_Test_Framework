import os
from selenium import webdriver
from common.element_excel_utils import ElementExcelUtil
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage

class ProjectPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 项目页面元素
        elements = ElementExcelUtil('project_page').get_elemnet_info()
        self.team_menu = elements['team_menu']

    def goto_team_menu(self):
        self.click(self.team_menu)

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
    # 进入项目菜单
    main_page = MainPage(driver)
    main_page.goto_project()
    # 进入团队菜单
    team = ProjectPage(driver)
    team.goto_team_menu()