#coding=utf-8

def main1():
    f = open(r"C:\Users\oceangene_ZX\Desktop\uuu-medical.medical_data_diping.csv")
    newfile = open(r"D:\study_Progame\testfile\newfile111.txt", "w")

    for eachline in f:
        list1 = eachline.split(",")
        print(list1)
        for i in list1:
            if not i:
                list1[list1.index(i)] = "."



        # join_str = list1[0] + "\t" + list1[1] + "\n"
        join_str = "\t".join([list1[0],list1[1],list1[2],list1[3]])   #这样写也可以
        newfile.write(join_str)
    f.close()
    newfile.close()

if __name__ == "__main__":
    main1()