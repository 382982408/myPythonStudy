print("-------------------------1----------------------------")
a = 1
b = 1
def te():
    global b
    a = 2
    b = 2

te()
print(a,b)

print("-------------------------2----------------------------")

class Tet1:
    a1 = 1
    b1 = 1
    def tt(self):
        self.a1 = 2
        self.b1 =2

test = Tet1()
print(test.a1,test.b1)

print("-------------------------3----------------------------")

class Tet2:
    a2 = 1
    b2 = 1
    def __init__(self):
        self.a2 = 2
        self.b2 =2

test = Tet2()
print(test.a2,test.b2)
print(a2,b2)