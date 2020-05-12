#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: login_test.py
# @time:2020/5/11 23:44
import unittest

from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_util import ConfigUtil
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_util import TestDataUtil

class LoginTest(SeleniumBaseCase):

    def setUp(self) -> None:
        super().setUp()
        self.test_class_date = TestDataUtil('login_suite','LoginTest').convert_exceldata_to_testdata() # 重载

    def test_login_success(self):
        test_function_data = self.test_class_date['test_login_success']
        self._testMethodDoc = test_function_data['test_name']   #
        login_action = LoginAction(self.base_page.driver)
        main_page =login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        actual_result = main_page.get_username()
        self.assertEqual(actual_result,test_function_data['excepted_result'],'test_login_success用例执行失败')

    def test_login_fail(self):
        test_function_data = self.test_class_date['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        self.assertEqual(actual_result,test_function_data['excepted_result'],'test_login_fail用例执行失败')

if __name__ == '__main__':
    unittest.main()
