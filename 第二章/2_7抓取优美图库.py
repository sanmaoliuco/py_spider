# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 9:00
# @Author : San_mao_liu
# @File : 2_7抓取优美图库.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

res = requests.get(url, headers = header)
res.encoding = "utf-8"
# print(res.text)
page = BeautifulSoup(res.text, "html.parser")  # 指定html解析器
# print(page)
a = page.find("div", attrs={"class": "Clbc_Game_l_a"}).find_all("a")
# print(a)
s = set()
for href in a:
    # print(href.get('href'))
    s.add(href.get('href'))

pic_list = []

for s1 in s:
    urls = "https://www.umei.cc" + s1
    res1 = requests.get(urls, headers= header)
    res1.encoding = "utf-8"
    page1 = BeautifulSoup(res1.text,"html.parser")
    src = page1.find("div", class_ = "big-pic").find("img").get('src')

    pic_list.append(src)

for pic in pic_list:
    img_res = requests.get(pic,headers = header)
    img_name = pic.split("/")[-1]
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_res.content)
    time.sleep(1)
# print(pic_list)
res.close()


