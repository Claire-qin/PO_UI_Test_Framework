import os
from selenium import webdriver
from common.element_excel_utils import ElementExcelUtil
from common.base_page import BasePage
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage

class AddProjectPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 添加项目页面元素信息
        elements = ElementExcelUtil("add_project_page").get_elemnet_info()
        self.project_create_button = elements['project_create_button']
        self.project_title_inputbox = elements['project_title_inputbox']
        self.project_code_inputbox = elements['project_code_inputbox']
        self.begin_date_inputbox = elements['begin_date_inputbox']
        self.end_date_inputbox = elements['end_date_inputbox']
        self.team_title_inputbox = elements['team_title_inputbox']
        self.project_type_select = elements['project_type_select']
        self.related_product_popup = elements['related_product_popup']
        self.related_product = elements['related_product']
        self.project_description_inputbox = elements['project_description_inputbox']
        self.access_control_chosen = elements['access_control_chosen']
        self.save_button = elements['save_button']

    def goto_add_project(self):  # 添加产品
        self.click(self.project_create_button)

    def input_project_title(self,title):  # 产品名称输入
        self.input(self.project_title_inputbox,title)

    def input_project_code(self,code):   # 项目代号输入
        self.input(self.project_code_inputbox, code)

    def input_begin_date(self,begin_date):  # 开始日期
        self.input(self.begin_date_inputbox,begin_date)
        self.click(self.project_title_inputbox)

    def input_end_date(self, end_date):  # 截至日期
        self.input(self.end_date_inputbox, end_date)
        self.click(self.project_title_inputbox)

    def input_team_title(self,title):   # 团队名称
        self.input(self.team_title_inputbox,title)

    def select_project_type(self,value):    # 项目类型
        self.select_value(self.project_type_select,value)

    def choose_related_product(self):   # 关联产品 下拉选择
        self.click(self.related_product_popup)
        self.click(self.related_product)

    def input_project_description(self,content):  # 项目描述
        self.input(self.project_description_inputbox,content)

    def radio_access_control(self):  # 访问控制选择
        self.click(self.access_control_chosen)

    def clik_cave(self):
        self.click(self.save_button)

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    # 登录
    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/my')
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_login()
    # 进入项目页面
    main_page = MainPage(driver)
    main_page.goto_project()
    # 添加项目页面
    add_project_page = AddProjectPage(driver)
    add_project_page.goto_add_project()
    add_project_page.input_project_title('项目02')
    add_project_page.input_project_code('peoject02')
    add_project_page.input_begin_date('2020-05-25')
    add_project_page.input_end_date('2021-05-25')
    add_project_page.input_team_title('团队02')
    add_project_page.select_project_type('waterfall')   # waterfall 长期项目
    add_project_page.choose_related_product()
    add_project_page.input_project_description('项目描述')
    add_project_page.radio_access_control()
    add_project_page.clik_cave()