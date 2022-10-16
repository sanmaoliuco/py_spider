# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/10 16:18
# @Author : San_mao_liu
# @File : 6_requests入门01.py
# @Software: PyCharm

# pip:install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests

query = input("输入：")

url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={query}'

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
res = requests.get(url,headers = headers)
print(res.text)
