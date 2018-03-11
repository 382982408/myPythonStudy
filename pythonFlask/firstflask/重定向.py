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
    # 第二种重定向方式，推荐使用
    return redirect(url_for("login"))

    return u'这是首页'

@app.route('/login/')
def login():
    return u'这是登录页面'

#重定向的应用,判断用户是否已经登录，如果登录成功，则返回发布问答页面
@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return u'这是问答页面'
    else:
        return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)