dict1 = {"a":1,
         "b":2,
         "c":3,
         "d":4,
         "e":5}
for key in dict1:
    print(key)
    print(dict1[key])               #字典是无序的

#是都在字典内部
1 in dict1              #返回为False，只能对key判断
"a" in dict1
"f" in dict1

di = dict1.items()          #返回为key和value组合的元祖
for each in di:
    print(each)
