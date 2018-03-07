g = lambda x : 2 * x +1
print(g(5))    #当不使用时，垃圾清理器会自动清理这个函数

s = lambda x, y : x + y
print(s(1,2))