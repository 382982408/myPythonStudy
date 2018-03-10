#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/11

'''
url反转: 从视图函数到url的转换
反转url的用处：1.页面重定向； 2.跳转页面（比如登录之后的跳转）
'''

from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    print(url_for("my_list"))   #视图函数名需要加上引号；print在控制台输出
    print(url_for("artical", id="abc"))   #反转一个带有参数的视图函数，需要将参数写进去，不然会报错
    return "hello world!"

@app.route('/list/')
def my_list():
    return "list"

@app.route('/artical/<id>/')
def artical(id):
    return u'您请求的id是s%' % id

if __name__ == '__main__':
    app.run(debug=True)