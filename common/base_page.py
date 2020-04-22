import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #浏览器操作封装 ->二次封装
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址%s'%url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s'%value)
        return value

# element_info= {'element_name': '用户名输入框',
#                           'locator_type': 'xpath',
#                           'locator_value': '//input[@name="account"]',
#                           'timeout': 5}
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH

        element = WebDriverWait(self.driver, locator_timeout) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        logger.info('[%s]元素识别成功'%element_info['element_name'])
        return element

    def click(self, element_info):
        element = self.find_element(element_info)
        logger.info('[%s]元素点击成功' % element_info['element_name'])
        element.click()

    def input(self, element_info, content):
        element = self.find_element(element_info)
        logger.info('[%s]元素输入内容:%s' %(element_info['element_name'],content))
        element.send_keys(content)
