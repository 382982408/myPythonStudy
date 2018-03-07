def duolie():
    f = open(r"D:\study_Progame\testfile\去除文件多列\mRNA.txt","r")
    newfile = open(r"D:\study_Progame\testfile\去除文件多列\mRNA_new.txt","w")

    list1 = f.readline()
    listTem = list1.split('\t')

    index1 = listTem.index("id")
    index2 = listTem.index('TCGA-IN-7806-11A-01R-2055-13')
    index3 = listTem.index('TCGA-BR-7704-11A-01R-2055-13')
    index4 = listTem.index('TCGA-HU-A4GC-11A-11R-A251-31')
    index5 = listTem.index('TCGA-CG-5722-11A-02R-1602-13')
    index6 = listTem.index('TCGA-HU-A4GY-11A-11R-A36D-31')

    newfile.write("id"+'\t'+'TCGA-IN-7806-11A-01R-2055-13'+'\t'
                  +'TCGA-BR-7704-11A-01R-2055-13'+'\t'+'TCGA-HU-A4GC-11A-11R-A251-31'+'\t'
                  +'TCGA-CG-5722-11A-02R-1602-13'+'\t'+'TCGA-HU-A4GY-11A-11R-A36D-31'+'\n')

    for eachline in f:
        lineNOn = eachline.strip('\n')
        list1 = lineNOn.split('\t')
        list2 = [list1[index1],list1[index2],list1[index3],list1[index4],list1[index5],list1[index6]]
        joinstr = '\t'.join(list2) + "\n"
        newfile.write(joinstr)

    f.close()
    newfile.close()


def duolie380():

    fsample = open(r"D:\study_Progame\testfile\去除文件多列\samples.txt", "r")
    f = open(r"D:\study_Progame\testfile\去除文件多列\mRNA.txt", "r")
    newfile = open(r"D:\study_Progame\testfile\去除文件多列\mRNA_new_good.txt", "w")

    list1 = f.readline()
    list1t = list1.strip('\n').split('\t')

    listsample = fsample.readline()
    listsamplet = listsample.strip('\n').split('\t')

    listIndex = []
    for i in listsamplet:
        if i in list1t:
            listIndex.append(list1t.index(i))

    n = 1
    f.seek(0,0)
    for eachline in f:
        listWrite = []
        listline = eachline.strip('\n').split('\t')
        for indx in listIndex:
            listWrite.append(listline[indx])
        listWritestr = "\t".join(listWrite) + "\n"
        print(n)
        newfile.write(listWritestr)
        n += 1

    fsample.close()
    f.close()
    newfile.close()


if __name__ == "__main__":
    duolie380()