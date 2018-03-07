##finally后面无论是否报错都执行的代码
try:
    f = open('D:\\study_Progame\\test_try_finally.txt',"a")    # “a“  表示追加，文件不存在时，可自动创建
    f.write("how are you?")
    num_error = 1 + '1'
except TypeError as reason:
    print("类型错误，原因是：",reason)
finally:
    f.close()

    ### raise
    print("----------------------分隔符-------------------------")
    raise ZeroDivisionError("除数不能为0")