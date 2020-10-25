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
from ddt import ddt, data
from common.sendRequests import SendRequests
from common.excel_reader import ReadExcel
import warnings
# import os
# from get_path_info import get_Path

# file_xlsx = os.path.join(get_Path(), 'data', 'mc_lpn.xlsx')
#
# print(file_xlsx, '4')

testData = ReadExcel().read('mc_lpn.xlsx', 'Sheet1')

cookies = {
    'logId': '426b481b',
    'pp_user_id': '43508577064735267',
    'appid': 'wxed9d3e6dc4a3704f',
    'openid': 'o5sBys9oyRLcdz91FitDdTaRpfuY',
}


@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        pass

    @data(*testData)
    def test_qq_api(self, data1):

        request_obj = SendRequests().send(self.s, data1, cookies=cookies)
        print(request_obj.json())
        self.assertIn('成功', request_obj.text)
        #切割字符串取后面的部分

        expect_result1 = data1["expect_result"].split(":")[1]
        print(expect_result1)

        # #转换为字符串
        # expect_result = eval(expect_result1)
        # #print(expect_result)
        #
        # self.assertEqual(re.json()["reason"], expect_result, "返回错误,实际结果是%s"%re.json()["reason"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
