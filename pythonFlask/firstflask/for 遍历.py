#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/11

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():

    user = {
        'username' : 'zx',
        'age' : 25
    }

    websites = ["baidu.com", "google.com"]

    return render_template('index02.html',user=user, websites = websites)

if __name__ == '__main__':
    app.run(debug=True)