def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        s = fib(n - 1) + fib(n - 2)
        return s

number1 = int(input("please enter a number:"))
fibs1 = fib(number1)
print ("斐波拉契数列的和为：", fibs1)



#迭代方式实现

def f(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("wrong")
    while (n-2) > 0:
        n3 = n1 +n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3

number2 = int(input("please enter a number:"))
fibs2 = f(number2)
print("%d为迭代方法的斐波拉契数列的和" % fibs2)


#可以用n=35来测试 运算时间