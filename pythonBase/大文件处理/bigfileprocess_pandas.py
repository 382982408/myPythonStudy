#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/12

import pandas as pd
import os


def process():
    ## OSError: Initializing from file failed 会报错,这是有与读取的文件带了路径
    ##参考：http://blog.csdn.net/qq_28132591/article/details/72624841

    # path = r'D:\important\学习资料\服务器中的annovar\software\annovar\humandb'
    # data = pd.read_table(path + "\hg19_avsnp147.txt", iterator=True, header=None, encoding="utf-8", delimiter="\t")
    filename = r'D:\important\学习资料\服务器中的annovar\software\annovar\humandb\hg19_avsnp147.txt'

    pwd = os.getcwd()
    os.chdir(os.path.dirname(filename))
    #注意basename是去掉文件的目录路径
    data = pd.read_table(os.path.basename(filename), delimiter="\t")
    # chunk = data.get_chunk(4)
    # a = chunk[0]
    # if chunk[0] == 1
    data.columns = ['one','two','three','four','five']

    df = data[data['five'] == 'rs768019142']
    print(df)

if __name__ == '__main__':
    process()

