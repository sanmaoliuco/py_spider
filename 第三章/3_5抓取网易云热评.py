# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/10/12 16:16
# @Author : San_mao_liu
# @File : 3_5抓取网易云热评.py
# @Software: PyCharm

# 1. 找到未加密的参数                       # window.arsea(参数, xxxx,xxx,xxx)
# 2. 想办法把参数进行加密(必须参考网易的逻辑), params  => encText, encSecKey => encSecKey
# 3. 请求到网易. 拿到评论信息

import requests
from Cryptodome.Cipher import AES
from base64 import b64encode
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=1e360314ea1bbb17a0a627ecf5b1e515"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# post

data = {
    "csrf_token": "1e360314ea1bbb17a0a627ecf5b1e515",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}

e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = "d5bpgMn9byrHNtAh"
# "encSecKey": "495baaf25c8c6931b00d807392426c815245c075ed6bf6cfa80624d4a0f2034e70b5a63e3a0480475d70e02ab4999b8a0918e4486b26760bcae5086e5f4a0ebea80c594233e91ff3d7e2f4a11c8df2be86132819aa187742cfce123955d3fe6ff91bab122d14b4cf9d33d0069405f2e0b3832b1577b049c26066c7f0ae81005c"

def get_encSecKey():
    return "1b5c4ad466aabcfb713940efed0c99a1030bce2456462c73d8383c60e751b069c24f82e60386186d4413e9d7f7a9c7cf89fb06e40e52f28b84b8786b476738a12b81ac60a3ff70e00b085c886a6600c012b61dbf418af84eb0be5b735988addafbd7221903c44d027b2696f1cd50c49917e515398bcc6080233c71142d226ebb"

def get_params(data):  # 默认这里接收到的是字符串
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data,key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key = key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)   # 创建加密器
    bs = aes.encrypt(data.encode('utf-8'))  # 加密,加密内容长度为16的倍数
    return str(b64encode(bs),'utf-8')

def a(a):
    return a


"""
    function a(a = 16) {  # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,   # 随机数1.2345
            e = Math.floor(e),   # 取整 1
            c += b.charAt(e);    # 从b中xx位置取字符
        return c
    }
    function b(a, b) {  # a要加密的内容 ，b就是密钥
    
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)   # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {  # c是密钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC   # 模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d:数据, e:010001, f: ,g:
        var h = {}    # 空对象
          , i = a(16);  # i就是一个16位的随机值
        h.encText = b(d, g),  # g是密钥
        h.encText = b(h.encText, i),  # 返回的就是params  i也是密钥
        h.encSecKey = c(i, e, f),   # 得到的就是encSecKey  e,f是固定的，如果把i固定
        return h
    }
"""

resp = requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey" : get_encSecKey()
},headers = headers)
print(resp.text)

# bKB8t = window.asrsea(JSON.stringify(i7b), buU5Z(["流泪", "强"]),
# buU5Z(Rg1x.md), buU5Z(["爱心", "女孩", "惊恐", "大笑"]));




