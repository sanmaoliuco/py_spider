# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 10:29
# @Author : San_mao_liu
# @File : 2_9_xpath案例_猪八戒.py
# @Software: PyCharm

import requests
from lxml import etree

url ="https://taiyuan.zbj.com/search/service/?kw=saas"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

res = requests.get(url,header)
# print(res.text)
html = etree.HTML(res.text)

# divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div/div')
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
# print(divs)
for div in divs:
    price = div.xpath('./div/div[3]/div/span/text()')[0].strip("￥")
    # print(price)
    title = div.xpath('./div/div[3]/a/text()')[0]
    # print(title)
    com_name = div.xpath('./div/a/div[2]/div[1]/div/text()')[0]
    # '//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/div/a/div[2]/div[1]/div'
    # print(com_name)
    # break
    # location = div.xpath('./')
    print(f'{com_name} + {title} + {price}')


