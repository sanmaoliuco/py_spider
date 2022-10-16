# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/13 18:08
# @Author : San_mao_liu
# @File : 4_8_小说下载.py
# @Software: PyCharm

# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}  => 所有章节的内容(名称, cid)
# 章节内部的内容
# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}
import requests
import asyncio
import aiohttp
import json
import aiofiles
'''
1、同步操作：访问getCatalog 拿到所有章节的cid和名称
2、异步操作：访问getChapterContent  下载所有文章内容
'''

# def getCatalog(url,headers):
#     res = requests.get(url,headers = headers)
#     dic = res.json()
#     cata_list = []
#     for item in dic['data']['novel']['items']:
#         # print(item)
#         sdic = {}
#         sdic['title'] = item['title']
#         sdic['cid'] = item['cid']
#         cata_list.append(sdic)
#     return cata_list
#
# def getChapterContent(url,headers):
#     res = requests.get(url,headers = headers)
#     print(res.text)
#
#
#
#
# if __name__ == '__main__':
#     book_id = "4306063500"
#     url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"} '
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
#     }
#     cata_list = getCatalog(url,headers)
#     for key in cata_list:
#         cid = key['cid']
#         cha_url = 'http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|'+cid+',"need_bookinfo":1}'
#         getChapterContent(cha_url,headers)
#         print(cha_url)
#         break

async def aiodownload(cid,b_id,title):
    data = {
        'book_id':b_id,
        'cid':f'{b_id}|{cid}',
        'need_bookinfo':1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    # print(url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            dic = await res.json()
            # print(dic)
            async with aiofiles.open('西游记/'+title+'.txt',mode='w',encoding= 'utf-8') as f:
                await f.write(dic['data']['novel']['content'])


async def getcata_log(url):
    res = requests.get(url)
    dic = res.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(aiodownload(cid,b_id, title))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = '4306063500'
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getcata_log(url))


