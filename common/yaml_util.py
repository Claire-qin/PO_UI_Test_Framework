#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: yaml_util.py
# @time:2020/5/8 10:30 

import os
import yaml

class YamlUtil:
    def __init__(self,file_path):
        self.file = open(file_path, encoding='UTF-8')

    def load(self):
        element_infos = yaml.load(self.file, Loader=yaml.FullLoader)
        return element_infos

    @classmethod
    def load_dic(cls, file_path):
        """
        【类方法】加载yaml文件并返回字典数据
        :param file_path:文件路径
        :return:数据字典集合
        """
        file = open(file_path, encoding='UTF-8')
        return  yaml.load(file, Loader=yaml.FullLoader)

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, '..', 'element_infos_datas/login_page.yaml')
    yaml_util = YamlUtil(file_path)
    data = yaml_util.load()
    print(data)
    print('============================================')
    print(YamlUtil.load_dic(file_path))