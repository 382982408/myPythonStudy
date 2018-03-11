#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/11

from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    # 第一种重定向方式
    # return redirect('/login/')
    # 第二种重定向方式，优先考虑
    return redirect(url_for("login"))

    return u'这是首页'

@app.route('/login/')
def login():
    return u'这是登录页面'

if __name__ == '__main__':
    app.run(debug=True)