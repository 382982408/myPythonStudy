#coding:utf-8
'''
多重继承最好不要用，容易造成逻辑混乱
'''
class Father():
    def one(self):
        print("我是1")

class Mother():
    def two(self):
        print("我是2")

class Son(Father,Mother):
    pass


son = Son()
son.one()
print("--" * 20)
son.two()
