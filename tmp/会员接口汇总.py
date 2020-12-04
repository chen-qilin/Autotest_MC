#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chen_7_0
@file:会员接口汇总.py
@time:2020/11/16
"""


import ddt
import unittest
import requests

cookies = {
    'logId': 'f3b61cdb',
    '_region_code_': 'T02',
    'pp_phone_hash': '07c91bf0',
    'pp_user_hash': 'a2a2d22e6c',
    'pp_user_id': '55590352301593029',
    'appid': 'wx88f62889b30261ac',
    'openid': 'oCIPIjqda0WMxq_Qjhjgmy_KNRFs'
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'token': 'eyJjdXJyZW50Um9sZSI6IlJPTEVfQURNSU4iLCJleHBpcmVUaW1lIjoxNjA2NDY3MjI4MDAzLCJ1c2VySWQiOjR9',
    'Referer': 'http://112.124.209.229:9800/eventManage',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'http://112.124.209.229:9800',
}

# 88888888888888888888888

url = 'http://112.124.209.229:9800/stc_op/api/data-permission/project/event/addEvent'

# params = (
#     ('eventCode', 'chenauto0001'),
# )

for i in range(1):
    change_code = 'chenauto000' + str(i)

    data = {
        "pid":1,
        "code":change_code,
        "name":"chentest",
        "type":0,
        "customizedParams":[
            {
                "code":"cust01",
                "name":"a",
                "isEdit":'false',
                "enable":'true',
                "inputText":"a"
            },
            {
                "code":"cust02",
                "name":"自定义2",
                "isEdit":'false',
                "enable":'false',
                "inputText":"自定义2"
            },
            {
                "code":"cust03",
                "name":"自定义3",
                "isEdit":'false',
                "enable":'false',
                "inputText":"自定义3"
            },
            {
                "code":"cust04",
                "name":"自定义4",
                "isEdit":'false',
                "enable":'false',
                "inputText":"自定义4"
            },
            {
                "code":"cust05",
                "name":"自定义5",
                "isEdit":'false',
                "enable":'false',
                "inputText":"自定义5"
            }
        ],
        "description":"111"
    }

    try:
        response = requests.post(url=url, headers=headers, cookies=None, params=None, json=data, verify=False)
        response.encoding = 'utf-8'
        print(response.request.url)
        print(response.content)
    except Exception as e:
        print(e)
    finally:
        print('end.')

print('all over!')