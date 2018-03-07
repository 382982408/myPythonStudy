#通过列表对应关系来实现
brand = ["李宁","耐克","阿迪达斯","特步"]
slogen = ["一切皆有可能","Just do it","Impossible is nothing","非一般的感觉"]
print("特步的广告语是：",slogen[brand.index('特步')])


#通过字典来实现，字典由key和value组成，中间用：分开，用{}表示

dict1 = {"李宁":"一切皆有可能","耐克":"Just do it","阿迪达斯":"Impossible is nothing","特步":"非一般的感觉"}
print("特步的广告语是：",dict1["特步"])

#字典的另外定义方式 元祖一个（），mapping一个（），dict带一个（），所以共有三个括号
dict2 = dict((("李宁","一切皆有可能"),("耐克","Just do it"),("阿迪达斯","Impossible is nothing"),("特步","非一般的感觉")))
print(dict2["李宁"])


dict3 = dict.fromkeys(range(32),"赞")
for eachkey in dict3.keys():
    print(eachkey)

for eachvalue in dict3.values():
    print(eachvalue)

for eachitem in dict3.items():
    print(eachitem)