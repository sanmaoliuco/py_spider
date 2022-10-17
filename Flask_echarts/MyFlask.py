# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/17 21:01
# @Author : San_mao_liu
# @File : MyFlask.py
# @Software: PyCharm


from flask import Flask,render_template
import pandas as pd


app = Flask(__name__)

@app.route("/")
def show():

    data = pd.read_csv("2022票房数据.csv")
    data = data.rename(columns={"影片名称":"name","总票房（万）":"value"})
    data = data.to_dict(orient="records")

    return render_template('show.html',data = data)



if __name__ == '__main__':
    app.run(debug=True)











