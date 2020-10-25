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
import ddt
from common.request_sender import SendRequests
from common.excel_reader import ReadExcel
import warnings

# 读取excel中的测试数据
test_data = ReadExcel().read('mc_lpn.xlsx', 'Sheet1')

# 自定义cookie
cookies = {
    'logId': '426b481b',
    'pp_user_id': '43508577064735267',
    'appid': 'wxed9d3e6dc4a3704f',
    'openid': 'o5sBys9oyRLcdz91FitDdTaRpfuY',
}


@ddt.ddt
class MemberCenter(unittest.TestCase):
    """
        会员中心—车牌校验—接口测试
    """
    def setUp(self):
        self.s = requests.session()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        pass

    @ddt.data(*test_data)
    def test_mc_lpn(self, case_data):
        print(case_data)
        response_obj = SendRequests().send(self.s, case_data, cookies=cookies)
        response_dict = response_obj.json()

        # 期望结果code
        if case_data["expect_code"] == '':
            pass
        else:
            # print(type(case_data['expect_code']))
            expect = case_data['expect_code']
            response = response_dict['code']
            self.assertEqual(expect, response)

        # 期望结果data
        if case_data["expect_data"] == '':
            pass
        else:
            expect = case_data['expect_data']
            response = response_dict['data']
            self.assertEqual(expect, response)

        # 期望结果message
        if case_data["expect_msg"] == '':
            pass
        else:
            expect = case_data['expect_msg']
            response = response_dict['message']
            self.assertIn(expect, response)


if __name__ == '__main__':
    unittest.main(verbosity=2)
