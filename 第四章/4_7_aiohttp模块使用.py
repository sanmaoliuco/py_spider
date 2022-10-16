# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/13 17:32
# @Author : San_mao_liu
# @File : 4_7_aiohttp模块使用.py
# @Software: PyCharm

import asyncio
import aiohttp

urls = [
    "https://www.umei.cc/d/file/20221012/d8b5646f77e57c33ade02d4c3e240e02.jpg",
    "https://www.umei.cc/d/file/20221012/ec92ebae3e878c719d13f6cd4e27201a.jpg",
    "https://www.umei.cc/d/file/20221012/e7de00d98cece677e653c4768698a650.jpg"
]

async def download(url):
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            with open(name,mode='wb') as f:
                f.write(await res.content.read())

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # asyncio.run(main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())







