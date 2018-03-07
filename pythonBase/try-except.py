try:
    f = open("这个文件不存在.txt")
    print(f.read())
    f.close()
except OSError:
    print("文件出错了……")
print("----------------------分隔符-------------------------")
    #加上as reason

try:
    f = open("这文件不存在")
    print(f.read())
    f.close()
except OSError as reason:    #reason可以为任何名字
    print("文件出错，出错的原因是：",str(reason))

print("----------------------分隔符-------------------------")
    ###一个try接多个except
try:
    f = open("不存在的文件")       #在第一步就报错了
    print(f.read())
    f.close()
    sum_number = 1 + "1"       #这个报错不会有，因为第一行就报错了
except OSError as reason1:
    print("文件出错，出错的原因是：",str(reason1))
except TypeError as reason2:
    print("类型出错，出错的原因是：",str(reason2))

print("----------------------分隔符-------------------------")

try:
    sum_number = 1 + "1"       #如果把这个错误放到第一行，后面的报错不会出现，只会给这个报错
    f = open("不存在的文件")
    print(f.read())
    f.close()

except OSError as reason1:
    print("文件出错，出错的原因是：",str(reason1))
except TypeError as reason2:
    print("类型出错，出错的原因是：",str(reason2))

print("----------------------分隔符-------------------------")
    ###两个一起写，简写
try:
    f = open("不存在的文件")
    print(f.read())
    f.close()
    sum_number = 1 + "1"
except (OSError, TypeError):
    print("出错")

print("----------------------分隔符-------------------------")