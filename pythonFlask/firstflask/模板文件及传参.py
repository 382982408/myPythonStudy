#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/11

from flask import Flask,render_template

app = Flask(__name__)

#第一种传参方式,但是如果参数比较多的时候，这种方式不利于代码维护
@app.route('/')
def index():
    return render_template("index01.html", username = "zx", gender = "male", age = "25")

#第二种方式，字典传参
@app.route("/one")
def index1():
    class Person(object):
        name = u"张三"
        age = 18

    p = Person()
    context = {
        'username' : "zx",
        'gender' : "male",
        'age' : 25,
        'another' : p,
        'websites':{
            "baidu" : "www.baidu.com",
            "google" : "www.google.com",
        }
    }
    return render_template("index01.html", **context)   #注意**的用法

#注意，在HTML中访问对象或者字典的属性或value可以用.去访问，例如index01.html中的{{ another['name'] }}、{{ websites['baidu'] }}

if __name__ == '__main__':
    app.run(debug=True)