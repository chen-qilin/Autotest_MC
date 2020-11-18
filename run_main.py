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
import time
import unittest
import get_path_info
# from common.HTMLTestRunner_jpg import HTMLTestRunner
from common.HTMLTestReportCN import HTMLTestRunner
from common.log import logger
from config import read_config
from common.send_email import SendEmail

# 定位当前文件的路径
path = get_path_info.get_Path()

# 日志
log = logger

# 读取配置中的邮箱开关
on_off = read_config.ReadConfig().get_email('on_off')


def run_case(tmp_dir="testcase"):
    case_dir = path + "\\" + tmp_dir
    # print(case_dir, 'run_case')
    # test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="mc_lpn.py", top_level_dir=None)
    return discover


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = path + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    log.info('Start:' + 40*'*')
    log.info('Report_path:'+report_path)
    with open(report_path, "wb") as fp:
        runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'接口测试', verbosity=2)
        try:
            runner.run(run_case())
        except Exception as e:
            log.info('Error:%s' % e)

    if on_off == 'on':
        SendEmail().send_email(report_path)
        print(report_path)
    else:
        print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
