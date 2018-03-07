#coding:utf-8

'''
类的组合，例：一个水池中有多少个鱼和乌龟
'''

class Turtle():
    def __init__(self,x):
        self.num = x

class Fish():
    def __init__(self,y):
        self.num = y

class Pool():
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print("水池中一个有%s只乌龟，%s条鱼" % (self.turtle.num, self.fish.num))

pool = Pool(1,10)
pool.print_num()