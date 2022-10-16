# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/11 8:23
# @Author : San_mao_liu
# @File : 2_4豆瓣250.py
# @Software: PyCharm

import requests
import re
import csv
# url = "https://movie.douban.com/top250"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# res = requests.get(url, headers=header)
# print(res)

for i in range(0,250,10):
    urls= f"https://movie.douban.com/top250?start={i}"
    res = requests.get(urls, headers = header)
    obj = re.compile(r"<li>.*?<span class=.*?>(?P<name>.*?)</span>"
                     r".*?<br>(?P<year>.*?)&nbsp"
                     r".*?<span class=.*? property=.*?>(?P<rating_num>.*?)</span>"
                     r".*?<span>(?P<people_num>.*?)</span>",re.S)

    result = obj.finditer(res.text)
    # print(res.text)
    # i = 0
    f = open("data2.csv",mode="a+",encoding='utf-8')
    csvwriter = csv.writer(f)
    for title in result:
        # print(title.group('name') + title.group('year').strip()
        #       + "  "  +title.group('rating_num') + "  " + title.group("people_num"))
        # i += 1
        dic = title.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())

    f.close()

    # print(i)
    res.close()












