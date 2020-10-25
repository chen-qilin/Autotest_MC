#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: case_01.py
@time: 2018/3/16 10:58
"""
import unittest

import requests
from ddt import ddt,data,unpack
from common.sendRequests import SendRequests
from common.excel_reader import ReadExcel
import os
from get_path_info import get_Path

# print(os.file_xlsx.dirname(os.getcwd()))
print(os.getcwd(),'getcwd')
print(os.path.dirname(os.getcwd()), 'dir')
p_dir = get_Path()
print( os.path.split(os.path.realpath(__file__))[0])
file_xlsx = os.path.join(p_dir, 'data', 'qq_apiTest.xlsx')
print(file_xlsx, '4')
testData = ReadExcel.readExcel(file_xlsx, "Sheet1")

# @ddt
# class Test1(unittest.TestCase):
#
#     def setUp(self):
#         self.s = requests.session()
#
#     def tearDown(self):
#         pass
#
#     @data(*testData)
#     def test_qq_api(self,data):
#
#         re = SendRequests().sendRequests(self.s, data)
#         print(re.json())
#
#         #切割字符串取后面的部分
#         expect_result1 = data["expect_result"].split(":")[1]
#         #转换为字符串
#         expect_result = eval(expect_result1)
#         #print(expect_result)
#
#         self.assertEqual(re.json()["reason"], expect_result, "返回错误,实际结果是%s"%re.json()["reason"])
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
