#coding:utf-8

import random as r

class Fish():
    def __init__(self):
        self.x = r.randint(0,18)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是：",self.x, self.y)

class Goldfish(Fish):
    pass

class Shark1(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am eating.")
        else:
            print("I am full.")

class Shark2(Fish):
    def __init__(self):
        Fish.__init__(self)  #调用未绑定的父类方法，相当于Fish.__init__(Shark2)，这种方法不常用
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am eating.")
        else:
            print("I am full.")

class Shark3(Fish):
    def __init__(self):
        super().__init__() # 使用super函数，这个方法较常用
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("I am eating.")
        else:
            print("I am full.")

print("这是shark2-------- #调用未绑定的父类方法#")
shark2 = Shark2()
shark2.move()

print("这是shark3-------- #使用super函数#")
shark3 = Shark3()
shark3.move()

# init 重写了属性，没有了父类的属性，所以move方法报错
print("这是shark1-------会报错---")
shark1 = Shark1()
shark1.eat()
shark1.move()