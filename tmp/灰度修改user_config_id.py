#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chen_7_0
@file:pp用户获取.py
@time:2020/10/30
"""

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
    'Host': 'cloud.keytop.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-cn',
    # 'referer': 'https://ts.keytop.cn/stcfront_vip/Member/Standard?origin=05&choosePackage=0',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN',
    'accesstoken': 'Raz2FyxSllzSkEPbLrvVgLkCMlmSIkVUJnWFOjWMq5DlYsEnj0Jb7z7AGjrVTDprgxCAPM-DlxUWW13KY3rbiA==',
}

params = {
    "userId": '55590352301593029',
    'userConfigId': 19  # 灰度的user_config_id改这个参数！！！
}

url = 'https://cloud.keytop.cn/mc/config/cache/saveTrafficDateConfig'

response = requests.get(url=url, headers=headers, cookies=cookies, params=params, verify=False)
response.encoding = 'utf-8'
print(response.request.url)
print(response.content)
print('end.')
