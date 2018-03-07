f = open("D:\\test.txt")     #将test里面的i love you 重复100次写入到testwrite文件中
g = open("D:\\testwrite.txt","w")


#g.read() 将字符串写入文件；g.writelines()向文件中写入字符串序列
for i in range(100):
    gw = f.readline(2)+"\n"
    g.write(gw)
    f.seek(0,0)

f.close()
g.close()