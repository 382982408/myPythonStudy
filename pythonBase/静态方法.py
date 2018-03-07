class Person:
    grade = 1

    def __init__(self, name):
        self.name = name

    def sayHi(self):  # 加self区别于普通函数
        print ('Hello, your name is--', self.name)

    @staticmethod  # 声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
    def sayName():  # 使用了静态方法，则不能再使用self
        print ("my name is king")  # ,grade,#self.name

    @classmethod  # 类方法
    def classMethod(cls):
        print("class method")

    def other(self):
        print("other")

# p = Person("King")
# p.sayName()
# p.sayHi()
# p.classMethod()

print("-" * 50)

Person.classMethod()
Person.sayName()
Person.other()
Person.sayHi("king--")