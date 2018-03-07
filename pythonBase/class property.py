#coding:utf-8

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self,value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I am the 'x' property")

c = C()
c.setx(5)
print(c.getx())


#用了property之后也可以这样
print("方法二")
print(c.x)
c.x = 3
print(c.x)