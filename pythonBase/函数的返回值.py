def hello():
    print("hello world!")

def hello_return():
    print("hello world!")
    return "返回值"

temp = hello()
print(".............test start......................")
print(temp)    #返回为空
print(".............test end......................")


temp2 = hello_return()
print(".............test start......................")
print(temp2)    #有返回
print(".............test end......................")
