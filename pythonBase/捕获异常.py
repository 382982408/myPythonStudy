#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/25


def error():
    try:
        print('test')
        raise Exception('zheliyouge yichang')
    except Exception as e:
        print(e)
        print('hello world')

def error1():
    try:
        print('test')
        a = 2
        b = 0
        print(a/b)
    except Exception as e:
        print(e)
        print('hello world')

def error2():
    a = True
    b = False
    assert a
    assert b


if __name__ == '__main__':
    error2()