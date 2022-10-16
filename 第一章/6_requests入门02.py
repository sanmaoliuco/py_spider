# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/10 16:39
# @Author : San_mao_liu
# @File : 6_requests入门02.py
# @Software: PyCharm

import requests

url = "https://fanyi.baidu.com/sug"

s = input("words: ")
data = {
    "kw":s
}

# 发送post请求，发送的数据必须放在字典中，通过data参数进行传递
res = requests.post(url,data=data)
print(res.json())  # 返回json文件
