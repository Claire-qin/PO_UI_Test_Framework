#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: element_data_util.py
# @time:2020/5/8 10:49

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common import HTMLTestReportCN
from common.log_util import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from common.config_util import cfg

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 浏览器操作封装 -- > 二次封装
    def open_url(self, url):
        try:
            self.driver.get(url)
            logger.info('打开url地址 %s ' % url)
        except Exception as e:
            logger.error('不能打开指定的测试网址，原因是：%s' % e.__str__())

    def close_tab(self):
        self.driver.close()
        logger.info('关闭当前的tab页签')

    def exit_driver(self):
        self.driver.quit()
        logger.info('退出浏览器')

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def implicitly_wait(self, seconds=cfg.time_out):
        self.driver.implicitly_wait(seconds)

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是%s' % value)
        return value

    def get_attribute_title(self, element_info):
        element = self.find_element(element_info)
        value = element.get_attribute('title')
        logger.info('[%s]元素获取其属性值是：%s' % (element_info['element_name'], value))
        return value

    def find_element(self, element_info):
        """
        根据提供的元素参数信息进行元素查找
        :param element_info:元素信息，字典类型{'element_name':'用户名输入框','locator_type':'xpath','locator_value':'//input[@name="account"]','timeout': 5 }
        :return: element对象
        """
        try:
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']
            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'name':
                locator_type = By.NAME
            elif locator_type_name == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'xpath':
                locator_type = By.XPATH
            element = WebDriverWait(self.driver, locator_timeout) \
                .until(lambda x: x.find_element(locator_type, locator_value_info))
            logger.info('[%s]元素识别成功' % element_info['element_name'])
            # element = WebDriverWait(self.driver, locator_timeout)\
            #     .until(EC.presence_of_element_located((locator_type, locator_value_info)))
        except Exception as e:
            logger.error('[%s]元素不能识别，原因是%s' % (element_info['element_name'], str(e)))
            self.screenshot_as_file()
        # finally:
        #     if element is None:
        #         element = ''
        return element

    def click(self, element_info):
        element = self.find_element(element_info)
        try:
            element.click()
            logger.info('[%s]元素进行点击操作' % element_info['element_name'])
        except Exception as e:
            logger.error('[%s]元素点击操作失败，原因是%s' % str(e))
            self.screenshot_as_file()

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s' % (element_info['element_name'], content))

    def get_text(self, element_info):
        element = self.find_element(element_info)
        return element.text

    def select_value(self, element_info, value):  # 下拉选择操作
        element = self.find_element(element_info)
        select_el = Select(element)
        time.sleep(1)
        select_el.select_by_value(value)
        logger.info('[%s]元素选择[%s]成功' % (element_info['element_name'], value))

    # 鼠标键盘封装
    def move_to_element_by_mouse(self, element_info):
        element = self.find_element(element_info)
        self.chains.move_to_element(element).perform()

    def long_press_element(self, element_info, senconds):
        element = self.find_element(element_info)
        self.chains.click_and_hold(element).pause(senconds).release(element)

    # selenium执行js
    def execute_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)

    def delete_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def delete_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value),
                                   element)

    # frame == > id/name   frame元素对象
    #    思路一
    def switch_to_frame(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    #   思路二
    def switch_to_frame_id_or_name(self, id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_by_element(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    #   思路三
    #
    # def switch_to_frame(self, **element_dict):  # switch_to_frame(id='frameid')  element=element_info
    #     self.wait(3)
    #     if 'id' in element_dict.keys():
    #         self.driver.switch_to.frame(element_dict['id'])
    #     elif 'name' in element_dict.keys():
    #         self.driver.switch_to.frame(element_dict['name'])
    #     elif 'element' in element_dict.keys():
    #         element = self.find_element(element_dict['element'])
    #         self.driver.switch_to.frame(element)

    # 弹出窗封装
    def switch_to_alert(self, action='accept', time_out=cfg.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        # self.wait(time_out)
        alter = self.driver.switch_to.alert
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
        return alter_text

    def get_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_window_by_title(self, title):
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, cfg.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_to_window_by_url(self, url):
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, cfg.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    def screenshot_as_file(self):
        report_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', cfg.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)

    # def screenshot_as_file_old(self, *screenshot_path):
    #     current_dir = os.path.dirname(__file__)
    #     if len(screenshot_path) == 0:
    #         screenshot_filepath = cfg.screenshot_path
    #     else:
    #         screenshot_filepath = screenshot_path[0]
    #     now = time.strftime('%Y_%m_%d_%H_%M_%S')
    #     screenshot_filepath = os.path.join(current_dir, '..', screenshot_filepath, 'UITest_%s.png' % now)
    #     self.driver.get_screenshot_as_file(screenshot_filepath)

    def wait(self, seconds=cfg.time_out):
        time.sleep(seconds)



