# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 11:33
# @Author : San_mao_liu
# @File : 3_2_模拟用户登录_处理cookie.py
# @Software: PyCharm

# 登录 -> 得到cookie
# 带着cookie 去请求到书架url -> 书架上的内容

# 必须得把上面的两个操作连起来
# 我们可以使用session进行请求 -> session你可以认为是一连串的请求. 在这个过程中的cookie不会丢失
import requests

# # 会话
# session = requests.session()
# data = {
#     "loginName": "18614075987",
#     "password": "q6035945"
# }
#
# # 1. 登录
# url = "https://passport.17k.com/ck/user/login"
# session.post(url, data=data)
# # print(resp.text)
# # print(resp.cookies)  # 看cookie
#
# # 2. 拿书架上的数据
# # 刚才的那个session中是有cookie的
# resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
#
# print(resp.json())

resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={
    "Cookie":"GUID=85d177a8-c091-4aa3-a416-f79ce73d7af5; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1665545487; __bid_n=183ca3f4346e06e3c34207; accessToken=nickname%3D%25E4%25B9%25A6%25E5%258F%258B5lPjEg81R%26avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F10%252F30%252F16%252F98971630.jpg-88x88%253Fv%253D1665545545029%26id%3D98971630%26e%3D1681097545%26s%3Dbb253a09f4850324; c_channel=0; c_csc=web; BAIDU_SSP_lcr=https://graph.qq.com/; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298971630%22%2C%22%24device_id%22%3A%22183ca3f429243d-0725afad87eaf7-c4b7526-2073600-183ca3f42934dd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2285d177a8-c091-4aa3-a416-f79ce73d7af5%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1665558525"
})
print(resp.text)






