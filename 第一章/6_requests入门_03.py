# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/10 17:16
# @Author : San_mao_liu
# @File : 6_requests入门_03.py
# @Software: PyCharm

import requests

url = "https://movie.douban.com/j/chart/top_list"

# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
user = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
res = requests.get(url = url, params=param,headers = user)

print(res.json())
res.close()