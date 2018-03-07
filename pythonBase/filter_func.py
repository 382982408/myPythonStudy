def is_odd(x):
    return x % 2 == 1

if __name__ == '__main__':
    print(list(filter(is_odd, [1, 4, 6, 7, 9, 12, 17])))