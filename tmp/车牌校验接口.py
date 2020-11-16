#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chen_7_0
@file:车牌校验接口.py
@time:2020/10/16
"""

import requests

cookies = {
    'logId': '426b481b',
    'pp_user_id': '43508577064735267',
    'appid': 'wxed9d3e6dc4a3704f',
    'openid': 'o5sBys9oyRLcdz91FitDdTaRpfuY',
}

headers = {
    'Host': 'ts.keytop.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-cn',
    'referer': 'https://ts.keytop.cn/stcfront_vip/Member/Standard?origin=05&choosePackage=0',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN',
    'accesstoken': 'Raz2FyxSllzSkEPbLrvVgLkCMlmSIkVUJnWFOjWMq5DlYsEnj0Jb7z7AGjrVTDprgxCAPM-DlxUWW13KY3rbiA==',
}

params = {
    '_': '1603159006345',
    'lpn': '川A07Y3港'
}
# cert = r'./charles-proxy-ca-9-2020-laptop-928qh8vi.pem'
url = 'https://ts.keytop.cn/mc/service/front/v2/openVip/bindLpnCheck'
response = requests.get(url=url, headers=headers, cookies=cookies, params=params, verify=False)

print(response.request.url)
print(response.text)
# print(response.content)
