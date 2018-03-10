#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/10

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

