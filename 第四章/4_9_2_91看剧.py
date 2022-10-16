# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/14 10:35
# @Author : San_mao_liu
# @File : 4_9_2_91看剧.py
# @Software: PyCharm

    # 1. 拿到548121-1-1.html的页面源代码
    # 2. 从源代码中提取到m3u8的url
    # 3. 下载m3u8
    # 4. 读取m3u8文件, 下载视频
    # 5. 合并视频

import requests
import re
from bs4 import BeautifulSoup
from Cryptodome.Cipher import AES
import asyncio
import aiohttp
import aiofiles
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# obj = re.compile(r'<script type=.*? >.*?"url":"(?P<url>.*?)".*?', re.S)  # 用来提取m3u8的url地址
# <script type"url":"https:\/\/v4.dious.cc\/20220516\/ZQnGvGIm\/index.m3u8","url_next"


# url = "http://www.gyzypx.cn/videoplay/26323-2-1.html"
# https:\/\/v4.dious.cc\/20220516\/ZQnGvGIm\/index.m3u8
# https://v4.dious.cc/20220516/ZQnGvGIm/1200kb/hls/index.m3u8
# resp = requests.get(url, headers=headers)


# result = obj.finditer(resp.text)
# m3u8_url = obj.search(resp.text).group('url')  # 拿到m3u8的地址
# # print(resp.text)
# m3u8_url_s = m3u8_url.replace('\\','')
# print(m3u8_url_s)
# print(result)
# resp.close()

# 下载m3u8文件
# m3u8_url="https://v4.dious.cc/20220516/ZQnGvGIm/1200kb/hls/index.m3u8"
# resp2 = requests.get(m3u8_url, headers=headers)
# # print(resp2.text)
# with open("纸牌屋/"+ "纸牌屋.m3u8", mode="wb") as f:
#     f.write(resp2.content)
# #
# resp2.close()
# print("下载完毕")


# 解析m3u8文件
# n = 1
# url_list = []
# with open("纸牌屋/纸牌屋.m3u8", mode="r", encoding="utf-8") as f:
#     for line in f:
#         line = line.strip()  # 先去掉空格, 空白, 换行符
#         if line.startswith("#"):  # 如果以#开头. 我不要
#             continue
        # https: // v4.dious.cc / 20220516 / ZQnGvGIm / 1200 kb / hls / FGd9qGet.ts
        # 下载视频片段
        # print(line)
        # line_url = "https://v4.dious.cc" + line
        # print(line_url)
        # url_list.append(line_url)
        # resp3 = requests.get(line,headers = headers)
        # print(resp3.text)
        # f = open(f"video/{n}.ts", mode="wb")
        # f.write(resp3.content)
        # f.close()
        # resp3.close()
        # n += 1
        # print(f"完成了{n}个")
# print(url_list)
# for url_line in url_list:
#     resp3 = requests.get(url = url_line,headers = headers)
#     with open(f'纸牌屋/{n}.ts',"wb") as f:
#         f.write(resp3.content)
#     resp3.close()
#     n += 1
#     print(f"完成了{n}个")





async def dec_ts(name,n):
    # print(n)
    aes = AES.new(key=b'50b554f888eecfd8', IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"纸牌屋/{n}.ts", mode="rb") as f1, \
        aiofiles.open(f"纸牌屋/temp_{n}.ts", mode="wb") as f2:
        # print('2')
        bs = await f1.read()  # 从源文件读取内容
        # print(bs)
        await f2.write(aes.decrypt(bs))  # 把解密好的内容写入文件
    print(f"{name}处理完毕")


async def aio_dec():
        # 解密
    tasks = []
    n = 1
    async with aiofiles.open("纸牌屋/纸牌屋.m3u8", mode="r", encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            # print(line)
                # 开始创建异步任务
            task = asyncio.create_task(dec_ts(line, n))
            n += 1
            if n > 436:
                break
            tasks.append(task)
        await asyncio.wait(tasks)


    # mac: cat 1.ts 2.ts 3.ts > xxx.mp4
    # windows: copy /b 1.ts+2.ts+3.ts xxx.mp4
    # lst = []
    # n = 1
    # with open("纸牌屋/纸牌屋.m3u8", mode="r", encoding="utf-8") as f:
    #     for line in f:
    #         if line.startswith("#"):
    #             continue
    #         line = line.strip()
    #         print(line)
    #         lst.append(f"纸牌屋/temp_{n}.ts")
    #         n += 1
    #         if n > 436:break
    # for n in range(1,437):
    #     lst.append(f"纸牌屋/temp_{n}.ts")

    # s = " ".join(lst)  # 1.ts 2.ts 3.ts
    # print(s)
    # os.system(f"copy /b {s} > movie.mp4")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio_dec())






















