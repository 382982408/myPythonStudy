#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/26

#带,的str转float或者int


if __name__ == '__main__':

    d = '1,2345.00'

    de = eval(d)

    print(de)

    print(type(de))


    print('%'*50)

    # 或者使用replace

    df = float(d.replace(',',''))
    print(df)
    print(type(df))

    ##eval和repr

    dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}

    dr = repr(dict1)        #repr将字典等格式转为str

    print("repr转换之后为",dr)
    print("repr转换之后为",type(dr))

    dev = eval(dr)      #eval将字符转为其他

    print("eval转换之后为",dev)
    print("eval转换之后为",type(dev))