#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chen_7_0
@file:111.py
@time:2020/10/26
"""
import re
import pymysql
import random
import uuid

from sshtunnel import SSHTunnelForwarder

# with SSHTunnelForwarder(
#         ('ssh-tunnel-16953.keytop.cn', 36893),  # B机器的配置
#         ssh_username='ssh',
#         ssh_password='sS_hH#aA&369',
#         remote_bind_address=('rm-bp1r60w1kvb30o250.mysql.rds.aliyuncs.com', 3306)) as server:  # A机器的配置
#
#     db_connect = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
#                                  port=server.local_bind_port,
#                                  user='root',
#                                  passwd='Keytop@123',
#                                  db='superpark_wx_test')

    cur = db_connect.cursor()
    print('connect success.')
    with open('../test1.txt', 'a') as f:
        coupon_info = '[{"couponCfgId":"MONTHLY_PERCENT_10_CUT","couponCount":1,"couponName":"月度九折优惠券","cvcId":"3","discount":9.0,"maxDiscountAmount":10000}]'
        data_list = []
        for i in range(5282):
            uid = str(uuid.uuid4())
            random_id = ''.join(uid.split('-'))
            data_list.append(
                (random_id, '43508577064735267', 1, '2020-10-26 00:00:00', '000202010208774099', '1',
                 pymysql.escape_string(coupon_info), '2020-12-20 10:05:10')
            )
        # print(data_list)
        f.write('%s\n' % random_id)
        # print(result)
        # print(pymysql.escape_string(coupon_info))
        print('*************')
        # executemany这家伙太坑了，正则，只能匹配%s，我输入%d或者直接是数字，都不行-_-!
        temp = "INSERT INTO `superpark_wx_test`.`mc_monthly_vip_send_coupon_plan`(`ID`, `USER_ID`, `SEND_TYPE`, `PLAN_SEND_TIME`, `ORDER_NO`, `CVC_ID`, `COUPON_INFO`, `DISABLE_TIME`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.executemany(temp, data_list)
        # print(result)
        db_connect.commit()
        print('commit.')
        cur.close()
        db_connect.close()


# temp = "INSERT INTO `superpark_wx_test`.`mc_monthly_vip_send_coupon_plan`(`ID`, `USER_ID`, `SEND_TYPE`, `PLAN_SEND_TIME`, `ORDER_NO`, `CVC_ID`, `COUPON_INFO`, `DISABLE_TIME`) VALUES(%s,%s,%s,%s,%s,%s,%s);"
# xxx = re.compile(
#     r"\s*((?:INSERT|REPLACE)\b.+\bVALUES?\s*)" +
#     r"(\(\s*(?:%s|%\(.+\)s)\s*(?:,\s*(?:%s|%\(.+\)s)\s*)*\))" +
#     r"(\s*(?:ON DUPLICATE.*)?);?\s*\Z",
#     re.IGNORECASE | re.DOTALL)
# print(xxx.match(temp))