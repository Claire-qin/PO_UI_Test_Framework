#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: run_all_cases.py
# @time:2020/5/12 23:01

import os
import unittest
from common import HTMLTestReportCN
from common.config_util import cfg
from common import zip_util
from common.email_util import EmailUtils

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join(current_path, '..', cfg.case_path)
report_path = os.path.join(current_path, '..', cfg.report_path)

class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path  = report_path
        print(case_path)
        print(report_path)

        self.title = '禅道自动化测试报告'
        self.description = '测试报告'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)  # 加载测试集合
        # HTMLTestReportCN执行测试用例
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path) # 自定义测试报告目录
        report_dir.create_dir(self.title)# 创建目录
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path') #报告的目录

        fp = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='qch')
        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__ == '__main__':
    dir_path = RunAllCases().run()
    report_zip_path = dir_path+'/../禅道自动化测试报告.zip'
    zip_util.zip_dir(dir_path,report_zip_path)
    EmailUtils('python自动化测试报告',report_zip_path).send_mail()