#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/2

'''
实验楼竞赛题目：制作一个不可改变的字典
'''

class ImmutableDict(dict):
    def pop(self, k):
        try:
            raise Exception('错误')
        except Exception as e:
            print(e)

    def clear(self):
        raise Exception('错误')

    def __delitem__(self, key):
        raise Exception('错误')

    def __setitem__(self, key, value):
        raise Exception('错误')







if __name__ == '__main__':
    a = {'one':1, 'two':2, 'three':3}
    d = ImmutableDict(a)

    # d.pop('one')
    d['four'] = 4

    print(d)

