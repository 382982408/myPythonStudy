'''
爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；
若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
'''


a = 0
list1 = []
while a <= 1000:
    if (a % 2 == 1) and (a % 3 == 2) and (a % 5 == 4) and (a % 6 == 5) and (a % 7 == 0):
        # print("yes")
        # print(a)
        list1.append(a)
        a += 1
    else:
    #     print("NO")
        a += 1
    # if a == 100:
    #     print(list1)

print(list1)