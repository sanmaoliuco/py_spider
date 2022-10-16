# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 20:05
# @Author : San_mao_liu
# @File : 4_3_多进程.py
# @Software: PyCharm


from multiprocessing import Process
from threading import Thread


def func(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    # p = Process(target=func)
    # p.start()
    # for i in range(1000):
    #     print("主进程",i)
    t1 = Thread(target=func, args=("周杰伦",))   # 参数得是元组
    t2 = Thread(target=func, args=("ling",))
    t1.start()
    t2.start()










