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
import ddt
import unittest
import requests
import warnings
from common.request_sender import RequestSender
from common.excel_reader import ExcelReader


# 读取excel中的测试数据
test_data = ExcelReader().read('mc_lpn.xlsx')


@ddt.ddt
class MemberCenter(unittest.TestCase):
    """
        会员中心—车牌校验—接口测试
    """
    def setUp(self):
        self.session_obj = requests.session()
        warnings.simplefilter('ignore', ResourceWarning)

    @ddt.data(*test_data)
    def test_mc_lpn(self, case_data):
        """
        车牌校验接口
        """
        print(case_data)
        response_result = RequestSender().send(self.session_obj, case_data)

        # 期望结果code
        if case_data["expect_code"] == '':
            pass
        else:
            # print(type(case_data['expect_code']))
            expect = case_data['expect_code']
            response = response_result['code']
            self.assertEqual(expect, response)

        # 期望结果data
        if case_data["expect_data"] == '':
            pass
        else:
            expect = case_data['expect_data']
            response = response_result['data']
            self.assertEqual(expect, response)

        # 期望结果message
        if case_data["expect_msg"] == '':
            pass
        else:
            expect = case_data['expect_msg']
            response = response_result['message']
            self.assertIn(expect, response)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
