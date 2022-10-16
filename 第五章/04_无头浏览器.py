# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/15 19:49
# @Author : San_mao_liu
# @File : 04_无头浏览器.py
# @Software: PyCharm


"""
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

# 准备好参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")

web = Chrome(options=opt)  # 把参数配置设置到浏览器中

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

time.sleep(2)
# # 定位到下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装, 包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器进行调整选项
# for i in range(len(sel.options)):  # i就是每一个下拉框选项的索引位置
#     sel.select_by_index(i)  # 按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]/table')
#     print(table.text)  # 打印所有文本信息
#     print("===================================")
#
# print("运行完毕.  ")
# web.close()


# 如何拿到页面代码Elements(经过数据加载以及js执行之后的结果的html内容)
print(web.page_source)


"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# # 定位到下拉列表
# sel_le = web.find_element(By.XPATH,'//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下来菜单
# sel = Select(sel_le)
# # 让浏览器进行调整选项
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(2)
#     table = web.find_element(By.XPATH,'//*[@id="TableList"]')
#     print(table.text)
#     print("=============================")
# web.close()

print(web.page_source)







