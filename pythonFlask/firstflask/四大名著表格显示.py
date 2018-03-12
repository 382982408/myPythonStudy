#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/11

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():

    books = [
        {
            'bookname' : '西游记',
            'author' : '吴承恩',
            'price' : 109
         },
        {
            'bookname': '红楼梦',
            'author': '曹雪芹',
            'price': 159
        },
        {
            'bookname': '三国演义',
            'author': '罗贯中',
            'price': 199
        },
        {
            'bookname': '水浒传',
            'author': '施耐庵',
            'price': 139
        },
    ]

    return render_template('fourbooks.html', books = books)

if __name__ == '__main__':
    app.run(debug=True)