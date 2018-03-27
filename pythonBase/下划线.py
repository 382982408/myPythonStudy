#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/27

'''
_halfprivate_method()可以直接访问，确实是。不过根据python的约定，应该将其视作private，而不要在外部使用它们，
（如果你非要使用也没辙），良好的编程习惯是不要在外部使用它。同时，根据Python docs的说明，_object和__object的作用域限制在本模块内。
'''
class A(object):

    def __init__(self):
        pass

    def __fullprivate(self):
        print('This is double underscore leading method')

    def public(self):
        print("This is public method")

    def _halfprivate(self):
        print('This is one underscore leading method')

if __name__ == '__main__':
    a = A()
    a.public()
    a._halfprivate()
    a.__fullprivate()
