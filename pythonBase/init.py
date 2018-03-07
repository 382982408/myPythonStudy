'''
__init__用于向class里面穿值
'''
class Human:
    name = "ren"
    gender = 'male'
    age = 25
    __money = 5000

    def __init__(self,a,b):
        print('#'*50)
        self.name = a
        self.age = b
        # Human.age = 40
        print('#'*50)

    def say(self):
        print('my name is %s and I have %d' % (self.name,self.__money))
        self.__lie()

    def __lie(self):
        print("I have 5000")

zhangsan = Human("zhangsan",30)
print(zhangsan.name,zhangsan.age,Human.age)