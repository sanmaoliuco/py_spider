# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/15 20:12
# @Author : San_mao_liu
# @File : 05_破解验证码利器.py
# @Software: PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.keys import Keys

import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('sanmaoliu', 'zxj5840119', '940082')

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)
def web_driver():

    web.get("https://kyfw.12306.cn/otn/resources/login.html")
    time.sleep(2)
    web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys("15635414062")
    web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('zxj5840119_')
    web.find_element(By.XPATH,'//*[@id="J-login"]').click()
    time.sleep(5)
    btn = web.find_element(By.XPATH,'//*[@id="nc_1__scale_text"]/span')
    ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()

    time.sleep(15)

    web.find_element(By.CLASS_NAME,"modal-close").click()
    btn1 = web.find_element(By.XPATH,'//*[@id="J-chepiao"]/a')
    ActionChains(web).move_to_element(btn1).perform()
    web.find_element(By.XPATH,'//*[@id="megamenu-3"]/div[1]/ul/li[1]/a').click()
    time.sleep(3)
    web.find_element(By.XPATH,'//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()

    web.find_element(By.ID,'fromStationText').click()
    web.find_element(By.ID,'fromStationText').send_keys('太原南',Keys.ENTER)
    web.find_element(By.ID,'toStationText').click()
    web.find_element(By.ID,'toStationText').send_keys('平遥古城',Keys.ENTER)
    web.find_element(By.XPATH,'//*[@id="query_ticket"]').click()
    time.sleep(5)
    web.find_element(By.XPATH,'//*[@id="ticket_49000D16360B_17_18"]/td[13]/a').click()
    time.sleep(2)
    web.find_element(By.XPATH,'//*[@id="normalPassenger_0"]').click()
    web.find_element(By.XPATH,'//*[@id="submitOrder_id"]').click()

    time.sleep(20)
    web.close()

if __name__ == '__main__':
    web_driver()









