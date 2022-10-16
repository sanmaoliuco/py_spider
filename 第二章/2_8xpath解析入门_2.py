# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 10:08
# @Author : San_mao_liu
# @File : 2_8xpath解析入门_2.py
# @Software: PyCharm

from lxml import etree

tree = etree.parse("b.html")
# res = tree.xpath("/html/body/ul/li/a/text()")
# res = tree.xpath("/html/body/ul/li[1]/a/text()")  # xpath的顺序是从1开始的，[]表示索引

# res = tree.xpath("/html/body/ol/li[2]/a[@href = 'dapao']/text()") # [@xxx=xxx] 属性的筛选
# print(res)

# ol_li_list =  tree.xpath("/html/body/ol/li")
# for li in ol_li_list:
#     # print(li)
#     res = li.xpath("./a/text()")
#     print(res)
#     href = li.xpath("./a/@href")
#     print(href)

print(tree.xpath("/html/body/ul/li/a/@href"))
print(tree.xpath("/html/body/div[1]/text()"))
print(tree.xpath("/html/body/ol/li/a/text()"))









