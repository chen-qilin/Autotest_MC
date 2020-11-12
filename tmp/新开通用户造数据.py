#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chen_7_0
@file:新开通用户造数据.py
@time:2020/11/12
"""

import re
import pymysql
import random
import uuid

db_connect = pymysql.connect(host='120.55.20.180', port =13308, user='root', passwd='Keytop@123',
                              db='superpark_wx_test')
print(db_connect)
# try:
#     pp_user = []
#     with open('./baoxian_user.txt', 'r', encoding='utf-8') as f:
#         for i in f.readlines():
#             i = i.replace('\n', '')
#             pp_user.append(i)
#
#     print(pp_user)
#
#     pp_credit_payment_id = []
#     with open('./baoxian_ppcreditid.txt', 'r', encoding='utf-8') as f:
#         for i in f.readlines():
#             i = i.replace('\n', '')
#             pp_credit_payment_id.append(i)
#
#     with db_connect.cursor() as cur:
#         cur = db_connect.cursor()
#         for i in range(50):
#             uid = str(uuid.uuid4())
#             random_id = ''.join(uid.split('-'))
#             print(random_id, pp_credit_payment_id[i])
#             try:
#                 res = cur.execute('INSERT INTO `superpark_wx_test`.`mc_user_vip_info`'
#                                   '(`id`, `pp_credit_payment_id`, `package_code`, `coupon_config_id`)'
#                                   ' VALUES(%s,%s,%s,%s);',
#                                   (random_id, pp_credit_payment_id[i], '01',  '1'))
#
#                 res2 = cur.execute('INSERT into  `parking_platform_test`.`pp_credit_payment`(`ID`,`USER_ID`,`PHONE`)'
#                                    'VALUES (%s,%s,%s)',
#                                    (random_id, pp_user[0], '15001111111'))
#                 db_connect.commit()
#             except Exception as e:
#                 print(e)
#         # res = cur.executemany(temp, data_list)
#         # res = cur.execute('select * from mc_user_vip_info')
#
# finally:
#     db_connect.close()


try:
    pp_credit_payment_id = []
    with open('./baoxian_ppcreditid.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.replace('\n', '')
            pp_credit_payment_id.append(i)

    with db_connect.cursor() as cur:
        temp = "UPDATE  `parking_platform_test`.`pp_credit_payment` set OPEN_TIME='2020-11-07 14:39:44' where `id` in (%s)"
        cur.executemany(temp, pp_credit_payment_id)

    db_connect.commit()

finally:
    db_connect.close()
