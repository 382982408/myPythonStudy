class Car:
    color = ""
    __money = 100000                    #私有属性
    baoxian = __money * 0.05  # 私有属性只能在内部使用

    def run(self):
        print("go,go,go!")

    def baoxianfee(self):
        baoxiantest = __money * 0.05  # 会报错，私有属性只能在内部使用
        # print("颜色是%s，价格是%d，保险费是%d" % (self.color,self.__money,self.__baoxiantest))

    def __baoxianfeePrivate(self):              #私有方法只能内部调用
        # baoxiantest = __money * 0.05  # 会报错，私有属性只能在内部使用
        print("颜色是%s，价格是%d，保险费是%d" % (self.color,self.__money,self.baoxian))


bmw = Car()         #实例化一个对象
bmw.color = "red"
print(bmw.color)

bmw.run()

print('---------------------分割线----------------------')
print(bmw.baoxian)                   #私有属性只能在内部使用
# print(bmw.__money)                   #会报错

print('---------------------分割线----------------------')
bmw.baoxianfee()
print('---------------------分割线----------------------')
bmw.__baoxianfeePrivate()