# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/11 9:10
# @Author : San_mao_liu
# @File : 2_5电影天堂.py
# @Software: PyCharm


import requests
import re

domain = "https://m.dytt8.net/index2.htm"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
res = requests.get(url=domain,headers = header)
# print(res.text)
res.encoding = "gb2312"
# print(res.text)
# obj1 = re.compile(r"2022新片精品.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"最新电影下载</a>]<a href='(?P<href>.*?)'>",re.S)
obj3 = re.compile(r'◎译　　名　(?P<movie>.*?).*?下载地址2：'
                  r'<a href="(?P<download>.*?)" target="_blank"  title="迅雷电影">',re.S)
result = obj2.finditer(res.text)
# print(i.group("ul") for i in result)
child_href_list = []
for it in result:
    child_href = 'https://m.dytt8.net/' + it.group('href').strip("/")
    child_href_list.append(child_href)
    # print(it.group('href'))
# print(res.text)
# print(child_href_list)
for hre in child_href_list:
    res1 = requests.get(hre,headers = header)
    res1.encoding = "gb2312"
    # print(res1.text)
    # break
    resu = obj3.search(res1.text)
    print(resu.group("movie"))
    print(resu.group("download"))

res.close()




