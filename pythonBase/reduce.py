from functools import reduce

def max_reduce(x,y):
    return max(x,y)


if __name__ == '__main__':
    lis = [1,2,3,4,5,1,2,3]
    print(reduce(max_reduce,lis))

    print(reduce(max,lis))