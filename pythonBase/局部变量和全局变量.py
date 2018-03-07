# def discounts(price,rate):
#     final_price = price * rate
#     return final_price
#
# old_price = float(input("please enter the price:"))
# sellrate = float(input("please enter the sell rate:"))
# new_price = discounts(old_price,sellrate)
# print("打折之后的价格为：",new_price)
#
# print("试图打印局部变量final_price",final_price)   #会报错，函数内的变量是用栈进行存储，在外部访问不到

##第二个例子
def example():
    global count   #  声明为全局变量
    count = 10
    print(count)

print("第二个例子")
count = 5
example()
print(count)

