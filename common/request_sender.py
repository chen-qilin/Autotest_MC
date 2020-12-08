# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: request_sender.py
@time: 2018/3/24 11:40
"""

import ast
import requests
from common.log import logger
from common.excel_reader import ExcelReader
# import json


class RequestSender:
    """
    封装request的请求对象
    """
    def __init__(self):
        self.logger = logger

    def send(self, session_obj, api_data, no_cookies='N', no_headers='N'):
        """
        从读取的Excel中获取响应的参数作为传递值，
        如果“用例.xlsx”的模板里没有填cookies或headers，
        就用从“basic_data.xlsx”里读默认的cookies或headers。
        """

        # ###########
        # 前期准备,处理各种数据
        # ##########

        # 获取http方法和url
        method = api_data["method"]
        url = api_data["url"]
        verify = False  # 不管https的安全提醒

        # 处理默认数据，目前只有默认cookies和默认headers
        basic_data = ExcelReader().read_basic_data('basic_data.xlsx')
        basic_cookies = basic_data[0]["cookies"]
        basic_headers = basic_data[0]["headers"]

        # 获取处理headers
        if no_headers == 'Y' or no_headers == 'y':
            headers = None
        else:
            if api_data["headers"] == '':
                headers = ast.literal_eval(basic_headers)
            else:
                headers = ast.literal_eval(api_data['headers'])

        # 处理cookies
        if no_cookies == 'Y' or no_cookies == 'y':
            cookies = None
        else:
            if api_data['cookies'] == '':
                cookies = ast.literal_eval(basic_cookies)
            else:
                cookies = ast.literal_eval(api_data['cookies'])

        # get方法的params参数，也有可能post方法带params（很不规范）
        if api_data["params"] == '':
            params = None
        else:
            params = ast.literal_eval(api_data['params'])

        # #################
        # requests的方法的处理
        # ################

        # get方法封装
        if method == 'get':
            # 真正的发起get请求
            request_obj = session_obj.request('get', url=url, headers=headers, params=params, verify=verify,
                                              cookies=cookies)

            # 响应结果，记录日志
            result = request_obj.json()
            self.logger.info('GET: '+str(url)+' :Params:'+str(params))
            self.logger.info('Result:' + str(result))

            # 返回响应结果
            return result

        # post方法封装
        elif method == 'post':
            # 获取post的data参数
            if api_data["post_data"] == '':
                post_data = {}
            else:
                post_data = ast.literal_eval(api_data['post_data'])

            # 真正的发起post请求
            request_obj = session_obj.request('post', url=url, headers=headers, params=params, json=post_data,
                                              verify=verify, cookies=cookies)

            # 响应结果，记录日志
            result = request_obj.json()
            self.logger.info('POST: ' + str(url) + ' Post_data:' + str(post_data))
            self.logger.info('Result: ' + str(result))

            # 返回响应结果
            return result

        # method只能是get或post
        else:
            self.logger.info('只支持get和post方法')
            raise Exception('Only support GET or POST method.')


if __name__ == '__main__':
    with requests.session() as s:
        test_data = ExcelReader().read('mc_lpn.xlsx')
        # print(testData)
        response = RequestSender().send(s, test_data[0])
        print(response)
