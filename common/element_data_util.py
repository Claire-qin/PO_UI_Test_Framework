#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: element_data_util.py
# @time:2020/5/8 10:49 

import os
from common.excel_util import ExcelUtil
from common.yaml_util import YamlUtil
from common.config_util import cfg

class ElementDataUtil:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_element_info_dic_by_excel(self, sheet_name, page_name):
        """
        通过excel文件获取元素信息字典
        :param sheet_name: sheet名称，为空时默认获取第一个sheet
        :param page_name: sheet页面中的pageName值
        :return: 返回sheetName中相关的pageName的元素信息字典
        """
        excel_util = ExcelUtil(self.file_path, sheet_name)
        sheet = excel_util.sheet_data
        element_infos = {}
        for i in range(1, sheet.nrows):
            if sheet.cell_value(i, 1) == page_name:
                element_info = {}
                element_info['element_name'] = sheet.cell_value(i, 2)
                element_info['locator_type'] = sheet.cell_value(i, 3)
                element_info['locator_value'] = sheet.cell_value(i, 4)
                timeout_value = sheet.cell_value(i, 5)
                element_info['timeout'] = timeout_value if isinstance(timeout_value, float) else cfg.time_out
                element_infos[sheet.cell_value(i, 0)] = element_info
        return element_infos

    def get_element_info_dic_by_yaml(self):
        """
        通过yaml文件获取元素信息字典
        :return: 返回相关内容字典
        """
        return YamlUtil.load_dic(self.file_path)


if __name__ == '__main__':
    element_data_util = ElementDataUtil(os.path.dirname(__file__) + '/../element_infos_datas/element_infos.xlsx')
    data = element_data_util.get_element_info_dic_by_excel("login","login_page")
    print(data)
    element_data_util = ElementDataUtil(os.path.dirname(__file__) + '/../element_infos_datas/login_page.yaml')
    data_yaml = element_data_util.get_element_info_dic_by_yaml()
    print(data_yaml)
