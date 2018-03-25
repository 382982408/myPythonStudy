#! usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhang xiong
# Time: 2018/3/12

def process():
    with open(r"D:\important\学习资料\服务器中的annovar\software\annovar\humandb\hg19_avsnp147.txt", "r") as database:
        with open("prefile.txt", "r") as data:
            n = 1
            print("正在处理第%s条" % n)
            for each_data in data:
                each_data_rs = each_data.strip("\n").split('\t')[0]

                for each_database in database:
                    each_database_rs = each_database.strip('\n').split('\t')[5]
                    if each_data_rs == each_database_rs:
                         print(each_database)

                n += 1

if __name__ == '__main__':
    process()

