'''
列表推导式和列表生成器的运行差别，前者比较耗内存耗时，
'''

#列表推导式
print(sum([i for i in range(1,10) if i % 3 == 0 or i % 5 == 0]))
print(sum([i for i in range(1,100) if i % 3 == 0 or i % 5 == 0]))
print(sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0]))
print(sum([i for i in range(1,10000) if i % 3 == 0 or i % 5 == 0]))
print(sum([i for i in range(1,100000) if i % 3 == 0 or i % 5 == 0]))
print(sum([i for i in range(1,1000000) if i % 3 == 0 or i % 5 == 0]))
print(sum([i for i in range(1,10000000) if i % 3 == 0 or i % 5 == 0]))  #运行时间有卡顿感

print("-------------------华丽的分割线------------------------")

#列表生成器

print(sum((i for i in range(1,10000000) if i % 3 == 0 or i % 5 == 0)))  #运行时间

#列表生成器其实返回为一个对象，并不会直接生成列表，只有每次向其索引的时候，才会一个个取出

gener = (i for i in range(1,100) if i % 3 == 0 or i % 5 == 0)
print(type(gener))                  #类型返回为generator
for i in gener:                     #只有每次索取时，才会给出值
    print(i)