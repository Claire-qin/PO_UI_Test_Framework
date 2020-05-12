#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: test_data_util.py
# @time:2020/5/11 21:39

import os
from common.excel_util import ExcelUtil
from common.config_util import cfg

current_path = os.path.abspath(os.path.dirname(__file__))
testdata_path = os.path.join(current_path, '..', cfg.testdata_path)

class TestDataUtil():
    def __init__(self,test_suite_name,test_class_name):
        self.test_class_name = test_class_name
        self.excel_data = ExcelUtil(testdata_path,test_suite_name).get_sheet_data_by_list()
        self.excel_rows = len(self.excel_data)

    def convert_exceldata_to_testdata(self):
    # {'test_login_success':
    #      {'test_name': '验证是否能成功进行登录', 'isnot': '是',
    #       'excepted_result': '测试人员1',
    #       'test_parameter': {'username': 'test01', 'password': 'newdream123'}
    #       }
    #  'test_login_fail':
    #      { }
    #  }
        test_data_infos ={}
        for i in range(1,self.excel_rows):   #1 2,去首行
            test_data_info ={}
            if self.excel_data[i][2].__eq__(self.test_class_name):    #等于
                test_data_info['test_name'] = self.excel_data[i][1]
                test_data_info['isnot'] = self.excel_data[i][3]
                test_data_info['excepted_result'] = self.excel_data[i][4]
                test_parameter = {}  # 存放测试参数
                for j in range(5,len(self.excel_data[i])):
                    if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j])>2:
                       parameter_info = self.excel_data[i][j].split('=')
                       test_parameter[parameter_info[0]] = parameter_info[1]
                test_data_info['test_parameter'] = test_parameter
            test_data_infos[self.excel_data[i][0]] = test_data_info
        return test_data_infos

if __name__ == '__main__':
    infos = TestDataUtil('login_suite','LoginTest').convert_exceldata_to_testdata()
    for i in infos.values():
        print(i)



