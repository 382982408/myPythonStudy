'''
Heroes beta-0.1
by xiong
2017年9月23日10:46:26
'''
hp = 100
print("welcome Heros world!")
name = input("input your name:")

if name:                               #或者写 if not name： name = “玩家一”
    pass
else:
    name = "玩家一"

usermsg = [name,hp]

print("你的英雄名是：{0};你的血是：{1}" .format(usermsg[0],usermsg[1]))

print("你的英雄名是：%s;你的血是：%s" %(usermsg[0],usermsg[1]))    #%d是指数字