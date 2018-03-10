#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/9

from flask import Flask,request,url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/user", methods=['POST'])
def hello_user():
    return 'hello user!'

@app.route('/user/<id>')
def user_id(id):
    return "hello user:" + str(id)

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return "query user : " + str(id)        #输入访问：http://127.0.0.1:5000/query_user?id=88889999

#反向路由 url_for
@app.route('/query_url')
def query_url():
    return 'query_url:' + url_for('query_user')


if __name__ == '__main__':
    app.run(debug=True)

