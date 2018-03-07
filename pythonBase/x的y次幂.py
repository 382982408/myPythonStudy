def power(x,y):
    '编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值'
    result = x ** y
    return result

if __name__ == "__main__":
    print(power(2,3))