def bingbao():
    value = int(input("请输入一个数字："))

    list_bingbao = []

    while True:                         #或者采用 while value != 1
        if value % 2 == 0:
            print(value)
            list_bingbao.append(value)
            value /= 2
        elif value % 2 == 1:
            if value == 1:
                list_bingbao.append(value)
                break
            else:
                print(value)
                list_bingbao.append(value)
                value = value * 3 + 1
    print(list_bingbao)

bingbao()