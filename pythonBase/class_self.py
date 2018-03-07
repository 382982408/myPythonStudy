class Ball:
    def setname(self,name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的，谁踢我……" % self.name)

a = Ball()
a.setname("球A")

b = Ball()
b.setname("球B")

c = Ball()
c.setname("土豆")


a.kick()
b.kick()
c.kick()


print("------------------分隔符----------------------------")

#__init__构建

class BALL:
    def __init__(self,name):
        self.name = name
    def KICK(self):
        print("我叫%s,该死的，谁踢我……" % self.name)

B = BALL("football")
B.KICK()

