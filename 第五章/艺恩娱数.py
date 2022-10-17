# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/17 15:28
# @Author : San_mao_liu
# @File : 艺恩娱数.py
# @Software: PyCharm

# import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.select import Select
import csv
import time

web = Chrome()

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")


options = web.find_element(By.XPATH,'//*[@id="OptionDate"]')
sel = Select(options)    # 对元素包装成下来列表
# num = web.find_element(By.XPATH,'//*[@id="TableList"]/table/tbody/tr[1]/td[4]').text
# print(num)
#
# print(sel)

for i in range(len(sel.options)):
    year = 2022 - i
    with open('data/' + f"{year}票房数据.csv",mode='w', encoding='utf-8') as f:
        writer = csv.writer(f)
        sel.select_by_index(i)   # 按照索引进行切换
        time.sleep(5)
        trs = web.find_elements(By.XPATH,'//*[@id="TableList"]/table/tbody/tr')
        # // *[ @ id = "TableList"] / table / tbody / tr[1]
        writer.writerow(['影片名称','总票房（万）'])
        for tr in trs:
            movie_name = tr.find_element(By.CLASS_NAME,'movie-name').text
            num = tr.find_element(By.XPATH,'./td[4]').text
            num1 = int(num.replace(',',''))
            writer.writerow([movie_name,num1])
            # print(movie_name,num1)
    time.sleep(2)

web.close()












