try:
    int(input("请输入："))      #可以试图输入abc或123
except ValueError as reason:
    print("出错啦"+str(reason))
else:
    print("没有发现任何异常")