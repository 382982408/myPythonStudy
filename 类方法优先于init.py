#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/10

'''
关于scrapy中，from_settings中的类方法如何调用，不懂……
参考:https://www.cnblogs.com/ruoniao/p/6906344.html
'''

class A():

    def __init__(self, a):
        self.a = 1

    @classmethod
    def B(cls):
        b = 23
        return b

    def get_value(self):
        print(self.a)

if __name__ == '__main__':
     c = A(1)
     print(c.get_value())



