#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site: 
@software: PyCharm
@file: run_main.py
@time: 2018/3/16 10:58
"""
import unittest
import time
import os
from common.HTMLTestRunner_jpg import HTMLTestRunner
import get_path_info

path = get_path_info.get_Path()


def run_case(dir="testcase"):
    case_dir = path + "\\" + dir
    # print(case_dir, 'run_case')
    # test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="case_02_qq.py", top_level_dir=None)
    return discover


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = path + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    with open(report_path, "wb") as fp:
        runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'接口测试', verbosity=2)
        runner.run(run_case())
