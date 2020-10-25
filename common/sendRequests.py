# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: sendRequests.py
@time: 2018/3/24 11:40
"""
from common.excel_reader import ReadExcel
import requests
import ast
import json


class SendRequests:

    def send(self, s, api_data, cookies=''):
        """
        从读取的表格中获取响应的参数作为传递
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

        # get方法
        if method == 'get':
            # get方法的params参数
            if api_data["params"] == '':
                params = None
            else:
                params = ast.literal_eval(api_data['params'])

            if cookies == '':
                request_obj = s.request('get', url=url, headers=headers, params=params, verify=verify)
            else:
                request_obj = s.request('get', url=url, headers=headers, params=params, verify=verify, cookies=cookies)
            return request_obj

        # post方法
        elif method =='post':
            pass
        else:
            print('只支持get和post方法')
            raise Exception('Only support GET or POST method.')
        # # 发送请求
        # if cookies == '':
        #     request_obj = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v)
        # else:
        #     if
        #     request_obj = s.request(method=method, url=url, headers=h, params=par, data=body, verify=v, cookies=cookies)
        # return request_obj

        # if api_data["params"] == "":
        #     par = None
        # else:
        #     par = eval(api_data["params"])
        #
        # if api_data["headers"] == "":
        #     h = None
        # else:
        #     h = eval(api_data["headers"])
        #
        # if api_data["body"] == "":
        #     body_data = None
        # else:
        #     body_data = eval(api_data["body"])


        # if 'type' in apiData.keys():
        #
        #     post_type = apiData["type"]
        #
        #     if post_type == "json":
        #         body = json.dumps(body_data)
        #         body = body_data
        #     if post_type == "data":
        #         body = body_data
        #     else:
        #         body = body_data
        # else:
        #     body = {}



if __name__ == '__main__':
    s = requests.session()
    testData = ReadExcel().read('test.xlsx')
    print(testData)
    response = SendRequests().send(s, testData[0])
    print(response.request.headers)
