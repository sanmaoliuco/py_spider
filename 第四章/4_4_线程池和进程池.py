# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 20:16
# @Author : San_mao_liu
# @File : 4_4_线程池和进程池.py
# @Software: PyCharm

# 线程池: 一次性开辟一些线程. 我们用户直接给线程池子提交任务. 线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name,i)


if __name__ == '__main__':
    # with ThreadPoolExecutor(50) as t:
    #     for i in range(100):
    #         t.submit(fn, name = f"线程{i}")
    # 等待线程池中的任务全部执行完毕，才继续执行（守护）

    with ProcessPoolExecutor(50) as p:
        for i in range(1000):
            p.submit(fn, name = f"进程{i}")

    print("123")




