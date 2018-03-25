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

def err():
    a = 1
    print('1111111111111')
    a += 1
    print('222222222222222222')
    a += 1
    print('33333333333333333333')
    a += 1
    print('4444444444444444444')
    a += 1
if __name__ == '__main__':
    err()