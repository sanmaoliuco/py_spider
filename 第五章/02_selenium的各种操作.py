# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/15 16:00
# @Author : San_mao_liu
# @File : 02_selenium的各种操作.py
# @Software: PyCharm

"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

web = Chrome()

web.get("http://lagou.com")

# 找到某个元素. 点击它
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')
el.click()  # 点击事件

time.sleep(1)  # 让浏览器缓一会儿

# 找到输入框. 输入python  =>  输入回车/点击搜索按钮
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(1)

# 查找存放数据的位置. 进行数据提取
# 找到页面中存放数据的所有的li
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_price = li.find_element_by_xpath("./div/div/div[2]/div/span").text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(company_name, job_name, job_price)

"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("http://lagou.com")

# 找到元素，点击
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[1]/a')
el.click()

time.sleep(1)
# 找到输入框，输入Python=》 输入回车/点击搜索按钮
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

time.sleep(1)
# 查找存放数据的位置，进行数据提取
# 找到页面中存放数据的所有的li
li_list = web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
# print(li_list)
for li in li_list:
    job_name = li.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    job_price = li.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    company_name = li.find_element(By.XPATH,'./div[1]/div[2]/div/a').text
    print(company_name,job_name,job_price)



















