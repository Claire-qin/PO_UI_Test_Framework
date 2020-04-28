import os
import time
from selenium import webdriver
from common.element_excel_utils import ElementExcelUtil
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from element_infos.project_page import ProjectPage

class ProjectTeamManagementPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 项目管理 页面元素
        elements = ElementExcelUtil('project_team_managemet').get_elemnet_info()
        self.team_manage_button = elements['team_manage_button']
        self.realname_dropdown = elements['realname_dropdown']
        self.realname_value = elements['realname_value']
        self.limited_user = elements['limited_user']
        self.delete_click = elements['delete_click']
        self.save_button = elements['save_button']
        self.add_button = elements['add_button']

    # 跳转团队管理页面
    def goto_team_manage(self):
        self.click(self.team_manage_button)

    def run(self):
        self.click(self.add_button)
        self.click(self.add_button)
        realname_dropdown_locator_value = self.realname_dropdown['locator_value']
        realname_value_locator_value = self.realname_value['locator_value']
        limited_user_locator_value = self.limited_user['locator_value']
        for i in range(0, 7):
            # //select[@onchange="setRole(this.value, 0)"]/../div[1]
            self.realname_dropdown['locator_value'] = realname_dropdown_locator_value % i
            self.click(self.realname_dropdown)
            time.sleep(0.5)
            self.realname_value['locator_value'] = realname_value_locator_value % (i, i+1)
            self.click(self.realname_value)
            value = 'yes'
            if i > 4:
                value = 'no'
            self.limited_user['locator_value'] = limited_user_locator_value % (i, value)
            self.click(self.limited_user)
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
    # 进入项目菜单
    main_page = MainPage(driver)
    main_page.goto_project()
    # 进入团队菜单
    team = ProjectPage(driver)
    team.goto_team_menu()
    time.sleep(1)
    # 团队管理
    team_management = ProjectTeamManagementPage(driver)
    team_management.goto_team_manage()
    team_management.run()
