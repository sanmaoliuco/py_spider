# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/16 9:14
# @Author : San_mao_liu
# @File : chaoji.py
# @Software: PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time


chaojiying = Chaojiying_Client('sanmaoliu', 'zxj5840119', '940082')

web = Chrome()

def chj():
    web.get('https://www.chaojiying.com/user/login/')
    img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
    dic = chaojiying.PostPic(img,1902)
    verify_code = dic['pic_str']

    web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('sanmaoliu')
    web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('zxj5840119')
    web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

    time.sleep(3)
    web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

if __name__ == '__main__':
    chj()
