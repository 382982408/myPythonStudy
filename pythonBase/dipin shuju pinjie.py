import re
def main1():
    f = open(r"D:\study_Progame\testfile\地贫ucsc坐标转换格式化\dipin_nosite.csv")
    newfile = open(r"D:\study_Progame\testfile\地贫ucsc坐标转换格式化\dipin_nosite_trans.txt", "w")

    for eachline in f:
        line = eachline.strip('\n')
        list1 = line.split(',')
        joinstr = 'chr16:' + list1[2] + "-" + list1[1] + '\n'
        newfile.write(joinstr)
    f.close()
    newfile.close()

def chaikai():
    f1 = open(r"D:\study_Progame\testfile\地贫ucsc坐标转换格式化\hg19_he_to_fenkai.csv")
    newfile1 = open(r"D:\study_Progame\testfile\地贫ucsc坐标转换格式化\hg19_over.txt", "w")
    newfile1.write('\t')
    next(f1)
    for line1 in f1:
        line2 = line1.strip('\n')
        list2 = re.split('[,:-]',line2)
        join_str = '\t'.join(list2) + '\n'
        newfile1.write(join_str)
    f1.close()
    newfile1.close()

if __name__ == '__main__':
    chaikai()
