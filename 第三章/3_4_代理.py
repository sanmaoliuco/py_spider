# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 15:58
# @Author : San_mao_liu
# @File : 3_4_代理.py
# @Software: PyCharm

# 通过第三方的机器去发送请求
#

import requests

# 120.24.76.81 	8123
proxies = {
    "https" : "https://47.100.137.173:666"
}

resp = requests.get("https://www.baidu.com")
resp.encoding = 'utf-8'
print(resp.text)


