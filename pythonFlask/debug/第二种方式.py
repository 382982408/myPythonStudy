#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/9

from flask import Flask
import config           #导入自定义的debug文件

app = Flask(__name__)
app.config.from_object(config)   #载入配置

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
