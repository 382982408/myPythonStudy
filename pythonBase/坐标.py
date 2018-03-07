def m1():
    for x1 in range(1,5):
        for y1 in range(1,5):
            print(x1,y1)

def m2():
    for x2 in range(1,5):
        for y2 in range(1,x2+1):
            print(x2,y2)

def m3():
    for x3 in range(1,5):
        for y3 in range(1,5):
            print(y3,x3)


if __name__ == '__main__':
    m3()
