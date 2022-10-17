# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/17 17:13
# @Author : San_mao_liu
# @File : MyFlask.py
# @Software: PyCharm

from flask import Flask,render_template,request

app = Flask(__name__)
#
# # 路由. 你通过浏览器访问过来的请求到底交给谁来处理
# @app.route("/")  # 写一个函数处理浏览器发送过来的请求
# def index():
#     # 业务处理
#     return "hello world"
#
# # 模板-》html
# @app.route("/")
# def index():
#     return render_template('hello.html')

# @app.route("/")
# def index():
#     s = "你好！"
#     lst = ['1','2','3']
#     return render_template('hello.html', jay = s, lst = lst)


# 登录验证
@app.route('/')
def index():
    return render_template("login.html")

@app.route("/login",methods = ['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("pwd")

    if username == 'alx' and password == '1233':
        return "success"
    else:
        return render_template('login.html', msg = "登录失败")



if __name__ == '__main__':

    app.run()







