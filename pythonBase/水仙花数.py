print("----------第一种方法--------------------")
for num in range(100,999):
    a = int(str(num)[0])
    b = int(str(num)[1])
    c = int(str(num)[2])
    if num == a**3 + b **3 + c **3:
        print(num)

print("----------第二种方法--------------------")

for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)
