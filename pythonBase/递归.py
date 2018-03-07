def fx(n):
    "求阶乘"
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def fn(g):
    "递归求阶乘"
    if g == 1:
        return 1
    else:
        return g * fn(g - 1)


d = fx(100)
print(d)

number = int(input("please input a number:"))
f = fn(number)
print(f)