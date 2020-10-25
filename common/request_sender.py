# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: request_sender.py
@time: 2018/3/24 11:40
"""

import requests
import ast
from common.log import logger
from common.excel_reader import ReadExcel
# import json


class SendRequests:
    """
    封装request的请求对象
    """
    def __init__(self):
        self.logger = logger

    def send(self, session_obj, api_data, cookies=''):
        """
        从读取的表格中获取响应的参数作为传递，cookie可以自己定义
        """

        # 获取http方法和url
        method = api_data["method"]
        url = api_data["url"]
        verify = False  # 不管https的安全提醒

        # 获取headers
        if api_data["headers"] == '':
            headers = None
        else:
            headers = ast.literal_eval(api_data['headers'])

        # get方法封装
        if method == 'get':
            # get方法的params参数
            if api_data["params"] == '':
                params = None
            else:
                params = ast.literal_eval(api_data['params'])

            # 根据cookie的情况，发起get请求
            if cookies == '':
                request_obj = session_obj.request('get', url=url, headers=headers, params=params, verify=verify)
                result = request_obj.json()
                self.logger.info('GET: '+str(url)+' :Params:'+str(params))
                self.logger.info('Result:' + str(result))
            else:
                request_obj = session_obj.request('get', url=url, headers=headers, params=params, verify=verify,
                                                  cookies=cookies)
                result = request_obj.json()
                self.logger.info('GET: '+str(url)+' :Params:'+str(params))
                self.logger.info('Result:' + str(result))
            return result

        # post方法封装
        elif method == 'post':
            # 如果有params就获取
            if api_data["params"] == '':
                params = None
            else:
                params = ast.literal_eval(api_data['params'])

            # 获取post的data参数
            if api_data["post_data"] == '':
                post_data = {}
            else:
                post_data = ast.literal_eval(api_data['post_data'])

            # 根据cookie的情况，发起post请求
            if cookies == '':
                request_obj = session_obj.request('post', url=url, headers=headers, params=params, json=post_data,
                                                  verify=verify)
                result = request_obj.json()
                self.logger.info('POST: ' + str(url) + ' Post_data:' + str(post_data))
                self.logger.info('Result: ' + str(result))
            else:
                request_obj = session_obj.request('post', url=url, headers=headers, params=params, json=post_data,
                                                  verify=verify, cookies=cookies)
                result = request_obj.json()
                self.logger.info('POST: ' + str(url) + ' Post_data:' + str(post_data))
                self.logger.info('Result: ' + str(result))
            return request_obj

        # method只能是get或post
        else:
            self.logger.info('只支持get和post方法')
            raise Exception('Only support GET or POST method.')


if __name__ == '__main__':
    with requests.session() as s:
        testData = ReadExcel().read('test.xlsx')
        print(testData)
        # response = SendRequests().send(s, test_data[0])
        # print(response.request.headers)
