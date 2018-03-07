#将列表a保存为文件
import pickle
a = [1,2,3,4,5,8,"一","i","love","you",["a","b"]]

pickle_file = open("D:\\pickfile.file","wb")    #创建一个可写的二进制文件

pickle.dump(a,pickle_file)    #将列表a装进文件对象中

pickle_file.close()

#将文件取出到列表b

pickle_fileb = open("D:\\pickfile.file","rb")   #注意这里这里用rb

b = pickle.load(pickle_fileb)

print(b)

pickle_fileb.close()