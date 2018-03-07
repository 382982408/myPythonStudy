#方法一
list1 = [1,1,1,2,2,3,4,12,12,5,3,6,8,10]
i = list1[0]
list_quchong = []
for i in list1:
        if i not in list_quchong:
            list_quchong.append(i)  ##为什么不能这样写？list_quchong = list_quchong.append(i),因为append 没有返回值
        else:
            continue
print(list_quchong)

#方法二，利用集合
list1_quchong_set = list(set(list1))
print(list1_quchong_set)