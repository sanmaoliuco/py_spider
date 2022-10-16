# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/13 16:51
# @Author : San_mao_liu
# @File : 4_6_协程.py
# @Software: PyCharm


# import time
#
# def func():
#     print("qwe")
#     time.sleep(3)  # 让当前的线程处于阻塞状态。CPU是不为工作
#     print('pppp')



# input() 程序也是处于阻塞状态
# requests.get(url)  在请求返回数据之前，程序也是处于阻塞状态
# 一般情况下，当程序处于IO操作的时候，可以选择性的切换到其他任务上

# 协程：当程序遇到IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务一起在执行
# 多任务异步操作

# 上述一切，都是在单线程的条件下
# import asyncio
#
# async def func():
#     print("asdf")
#
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)  # 协程程序运行需要asyncio模块的支持

# import asyncio
# import time
#
# async def func1():
#     print("as")
#     await asyncio.sleep(3)
#     print("as")
#
# async def func2():
#     print("po")
#     await asyncio.sleep(2)
#     print("po")
#
# async def func3():
#     print("we")
#     await asyncio.sleep(4)
#     print("we")
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     task = [f1, f2, f3]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(task))
#     t2 = time.time()
#     print(t2 - t1)

import asyncio
import time

async def func1():
    print("as")
    await asyncio.sleep(3)
    print("as")

async def func2():
    print("po")
    await asyncio.sleep(2)
    print("po")

async def func3():
    print("we")
    await asyncio.sleep(4)
    print("we")

async def main():
    # 第一种写法
    # f1 = func1()
    # await f1  # 一般await挂起操作放在协程对象前面
    # 第二种写法
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)











