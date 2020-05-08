#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: excel_util.py
# @time:2020/5/8 10:16 

import os
import xlrd
from common.config_util import cfg
from common.log_util import logger

class ExcelUtil(object):
    def __init__(self,excel_path,sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        if os.path.exists(self.excel_path):
            workbook = xlrd.open_workbook(self.excel_path)
            if self.sheet_name:     # 当sheet_name没带参数时，默认取第一个表格
                sheet = workbook.sheet_by_name(self.sheet_name)
            else:
                sheet = workbook.sheet_by_index(0)
            return sheet
        else:
            logger.error("文件不存在:%s"%self.excel_path)
            raise  Exception("文件不存在:%s"%self.excel_path)

    @property
    def get_row_count(self):
        row_count = self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count = self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self):
        """
        获取sheet数据以列表形式返回
        :return: 数据列表 [ [] , [] , [] ]
        """
        all_excel_data = []
        for rownum in range(self.get_row_count):
            row_excel_data = []
            for colnum in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(rownum,colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data