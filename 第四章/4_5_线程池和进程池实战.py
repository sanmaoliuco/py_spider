# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 20:23
# @Author : San_mao_liu
# @File : 4_5_线程池和进程池实战.py
# @Software: PyCharm

# 1. 如何提取单个页面的数据
# 2. 上线程池,多个页面同时抓取

import requests
from lxml import etree
import json
import jsonpath
import csv
from concurrent.futures import ThreadPoolExecutor



def download_one_page(url,headers,data):
    res = requests.post(url = url,headers = headers,data = data)
    # // *[ @ id = "tableBody"]
    jsonbj = json.loads(res.text)
    # print(jsonbj)
    # html = etree.HTML(res.text)
    # table = html.xpath('// *[ @ id = "tableBody"]/tr')
    # print(table)
    name = jsonpath.jsonpath(jsonbj,"$..prodName")
    lowPrice = jsonpath.jsonpath(jsonbj,"$..lowPrice")
    highPrice = jsonpath.jsonpath(jsonbj,"$..highPrice")
    place = jsonpath.jsonpath(jsonbj,'$..place')
    sclist = []
    for i in range(20):
        scdict = {}
        scdict['菜名'] = name[i]
        scdict['最低价'] = lowPrice[i]
        scdict['最高价'] = highPrice[i]
        scdict['产地'] = place[i]
        # print(scdict)
        # break
        sclist.append(scdict)
    # print(sclist)
    for j in sclist:
        with open('新发地.csv','a+',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(j.values())



if __name__ == '__main__':
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Referer": "http://www.xinfadi.com.cn/priceDetail.html"
    }

    with ThreadPoolExecutor(50) as p:
        for i in range(20):
            p.submit(download_one_page(url=url,headers = headers,data={
                "limit": "20",
                "current": i+1,
            }))