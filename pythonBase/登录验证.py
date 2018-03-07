'''
输入用户名和密码，输入三次锁定
'''
import os
welcome = "welcome to Heroes world!"

n = 0
while True:
    if os.path.isfile("lock.log"):
        print("locked")
        break
    username = input("login:")
    password = input("password:")
    n = n + 1

    if username == 'zhangxiong' and password == '11111111':
        pass
    else:
        if n == 3:
            open('lock.log','w').write(username)
            print('locked')
            break
        continue

    print(welcome)
    break