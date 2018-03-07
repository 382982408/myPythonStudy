#猜随机数
import random
def guess():
    try:
        symtem_number = random.randint(1, 10)
        while True:
            person_input = int(input("Please enter a number:"))
            if person_input \
                    == symtem_number:                                    # 加\可以使一行变多行执行
                print("You get it.Congratulations")
                break
            if person_input >= symtem_number:
                print("it is big")
            else:
                print("it is "
                      "small")                                   #括号也可以多行执行
    except ValueError as reason1:                                #reason1是个变量
        print("输入出错，出错的原因是：",str(reason1))


if __name__ == '__main__':
    guess()