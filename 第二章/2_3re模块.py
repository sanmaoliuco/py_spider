# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/10 17:54
# @Author : San_mao_liu
# @File : 2_3re模块.py
# @Software: PyCharm


import re
#
# # findall :匹配字符串中所有的符合正则的内容
# lst = re.findall(r'\d+',"phone num:123234,phn:343445545")
# print(lst)
# # finditer:匹配字符串中 所有的内容[返回的是迭代器] , 从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+","phone num:123234,phn:343445545")
# # print(it)
# for i in it:
#     print(i.group())



# search，找到一个结果就返回，返回的结果就是match对象。拿数据需要.group()
# s = re.search(r"\d+","phone num:123234,phn:343445545")
# print(s.group())

# match 从头开始匹配
# s = re.match(r"\d+","123234,phn:343445545")
# print(s.group())

# 预加载正则表达式
# obj = re.compile(r"\d+")

# res = obj.finditer("phone num:123234,phn:343445545")
# print(res)
# for i in res:
#     print(i)

# ree = obj.findall("phone num:123234,phn:343445545")
# print(ree)

s = """
<div class = 'jay'><span id = '1'>郭麒麟</span></div>
<div class = 'jf'><span id = '2'>宋轶</span></div>
<div class = 'jgy'><span id = '3'>郭德纲</span></div>
<div class = 'jpy'><span id = '4'>大聪明</span></div>

"""

# (?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取内容
# obj = re.compile(r"<div class = '.*?'><span id = '(?P<idnum>\d+)'>(?P<name>.*?)</span></div>",re.S)  # re.S : 让.能匹配换行符
#
# res = obj.finditer(s)
# for it in res:
#     print(it.group("idnum") + it.group("name"))

for i in range(0, 250, 25):
    print(i)





















