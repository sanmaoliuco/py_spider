# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/15 17:19
# @Author : San_mao_liu
# @File : 03_窗口切换.py
# @Software: PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
web = Chrome()

# web.get("http://lagou.com")
#
# web.find_element(By.XPATH,'//*[@id="cboxClose"]').click()
#
# time.sleep(1)
# web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)
# time.sleep(1)
# web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
#
# # 如何进入到新窗口
# # 在selenium中，新窗口是不会进行切换的
# web.switch_to.window(web.window_handles[-1])
#
# jd = web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]').text
# print(jd)
# web.close()
# web.switch_to.window(web.window_handles[0])
# print(web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text)

web.get('http://www.gyzypx.cn/videoplay/26323-2-1.html')

time.sleep(1)
# 处理iframe，先拿到iframe，然后切换到iframe中，再拿数据
iframe = web.find_element(By.XPATH,'//*[@id="playleft"]/iframe')
web.switch_to.frame(iframe)   # 切换到iframe
time.sleep(5)
web.find_element(By.CLASS_NAME,'outter').click()
# soup = BeautifulSoup(web.page_source,'lxml')
# print(soup)
# web.switch_to.default_content()   # 切换回原页面









