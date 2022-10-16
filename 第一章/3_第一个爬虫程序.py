# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/10 15:41
# @Author : San_mao_liu
# @File : 3_第一个爬虫程序.py
# @Software: PyCharm


from urllib.request import urlopen

url = "http://www.baidu.com"
res = urlopen(url)

with open("mybaidu.html", mode="w",encoding='utf-8') as f:
    f.write(res.read().decode("utf-8"))


























