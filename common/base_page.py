import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

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

#元素信息识别、操作

    #识别元素信息
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        is_iframe = element_info['is_iframe']
        iframe_id_name = element_info['iframe_id_name']
        iframe_locator_value = element_info['iframe_locator_value']

        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        #有无 iframe
        if is_iframe != 1:
            element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type, locator_value_info))
            logger.info('[%s]元素识别成功'%element_info['element_name'])
        elif is_iframe == 1 and iframe_id_name == '':  # iframe没有id或者name
            frame_element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type, iframe_locator_value)) #xpath识别iframe
            self.driver.switch_to.frame(frame_element)
            element = WebDriverWait(self.driver, locator_timeout).until(lambda x: x.find_element(locator_type, locator_value_info))
            logger.info('[%s]元素识别成功'%element_info['element_name'])
            # self.driver.switch_to.default_content()
        elif is_iframe == 1 and iframe_id_name != '':
            self.driver.switch_to.frame(iframe_id_name)
            element = WebDriverWait(self.driver, locator_timeout) .until(lambda x: x.find_element(locator_type, locator_value_info))
            logger.info('[%s]元素识别成功' % element_info['element_name'])
            # self.driver.switch_to.default_content()
        return element

    # 元素信息操作 封装 -》二次封装
    def click(self,element_info):
        is_iframe = element_info['is_iframe']
        element = self.find_element(element_info)
        logger.info('[%s]元素点击成功' % element_info['element_name'])
        element.click()
        if is_iframe == 1:
            self.driver.switch_to.default_content()

    def input(self,element_info, content):
        is_iframe = element_info['is_iframe']
        element = self.find_element(element_info)
        logger.info('[%s]元素输入内容：%s' % (element_info['element_name'],content))
        element.clear()
        element.send_keys(content)
        if is_iframe == 1:
            self.driver.switch_to.default_content()
        time.sleep(1)
    #
    def get_attribute_title(self,element_info):
        element = self.find_element(element_info)
        value = element.get_attribute('title')
        logger.info('[%s]元素获取其属性值是：%s' % (element_info['element_name'],value))
        return value

    def get_text(self,element_info):
        element = self.find_element(element_info)
        value = element.text
        logger.info('[%s]元素获取其文本内容是：%s' % (element_info['element_name'],value))
        return value

    def select_value(self,element_info,value):  # 下拉选择操作
        element = self.find_element(element_info)
        select_el = Select(element)
        time.sleep(1)
        select_el.select_by_value(value)
        logger.info('[%s]元素选择[%s]成功' % (element_info['element_name'],value))

    def clik_confirm_delete(self,element_info):
        elemnet = self.find_element(element_info)
        elemnet.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()  #确认删除
        logger.info('[%s]元素获取其文本内容是：%s' % (element_info['element_name'], element_info))



