class Father:
    money = 10000000
    __money = 100000000   #"父亲的私房钱"，私有属性

    def drive(self):
        print('I can drive a car')
class Mother:
    moneyM = 100000000              #如果两个父类的属性名一样，只能继承第一个
class Son(Father,Mother):               #可以同时继承两个
    pass
    def pay(self):
        print(self.__money)         #私有属性不能继承，出错

tom = Father()
print(tom.money)
tom.drive()

print('-' * 50)

littleTom = Son()
print(littleTom.money)
littleTom.drive()

print('#' * 50)
print(littleTom.moneyM)

print('#' * 50)
littleTom.pay()