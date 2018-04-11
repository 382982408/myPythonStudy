#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/4/11


def ye():
    for i in range(10):
        # yield 不会终止，继续执行，直至for循环完成，返回一个生成器
        yield i

def fun():
    for i in range(10):
        # return之后即终止，跳出循环
        return i


if __name__ == '__main__':
    print(fun())
    print(fun())

    print("*" * 50)

    print(ye())
    for i in ye():
        print(i)

    print(ye())
    for h in ye():
        print(h)
