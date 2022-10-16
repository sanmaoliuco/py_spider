# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 15:22
# @Author : San_mao_liu
# @File : 3_3防盗链的处理.py
# @Software: PyCharm

# 1. 拿到contID
# 2. 拿到videoStatus返回的json.-> srcURL
# 3. srcURL里面的内容进行修整
# 4. 下载视频

import requests
from lxml import etree

url = "https://www.pearvideo.com/video_1738587"
contId = url.split("_")[1]
videoStatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.9182961069911197"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    # 防盗链
    "Referer": url
}

video_n = requests.get(url,headers)
html = etree.HTML(video_n.text)
video_name = html.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]
# print(video_name)
res = requests.get(videoStatus, headers = headers)
# print(res.text)
dic = res.json()
# print(dic)
srcurl = dic['videoInfo']["videos"]["srcUrl"]
systemTime = dic['systemTime']
# print(srcurl,systemTime)

srcUrl = srcurl.replace(systemTime,f"cont-{contId}")

video_src = requests.get(srcUrl,headers)
# print(video_src)
# '//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1'
with open("video/" + video_name + ".mp4", mode="wb") as f:
    f.write(video_src.content)

