#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/10

from flask import Flask,render_template
from models import User

app = Flask(__name__)

#页面显示方法

#第一种方法，直接return
@app.route('/one')
def hello1():
    return "<h1>hello world</h1>"       #h1表示格式

#第二种方法,在html模板中定义
@app.route('/two')
def hello2():
    return render_template("index2.html")

#第三种方法，通过python传递到模板引擎中
@app.route('/three')
def hello3():
    content = 'hello world'
    return render_template('index3.html',content = content)

#第四种方法吗，将对象传入
@app.route('/four')
def hello_user():
    user1 = User(1, "NO1")
    return render_template("index4.html", user = user1)

#第五种，条件判断
@app.route('/five<id>')
def user_query(id):
    user = None
    if int(id) == 1:
        user = User(1, "NO1")
    return render_template('index5.html', user = user)

if __name__ == '__main__':
    app.run(debug=True)

