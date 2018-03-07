#从文件中读取两列放入新文件中

def main1():
    f = open(r"D:\study_Progame\testfile\OMIM_ALL_FREQUENCIES_diseases_to_genes_to_phenotypes.txt")
    newfile = open(r"D:\study_Progame\testfile\newfile.txt", "w")

    for eachline in f:
        list1 = eachline.split("\t")
        join_str = list1[0] + "\t" + list1[1] + "\n"
        # join_str = "\t".join([list1[0],list1[1]]) + "\n"  #这样写也可以
        newfile.write(join_str)
    f.close()
    newfile.close()

def main2():
    f = open(r"D:\study_Progame\testfile\OMIM_ALL_FREQUENCIES_diseases_to_genes_to_phenotypes.txt")
    count = 0
    for e in f:
        if not e.startswith('#'):
            if count < 100:
                line = e.split('\n')[0]
                list = line.split('\t')
                print(list)
        count += 1


if __name__ == '__main__':
    main2()