def collectionpara(*shoujicanshu):
    print("参数的长度是：",len(shoujicanshu))
    print("第二个参数是：",shoujicanshu[1])   #收集参数其实就是将所有参数都组成一个shoujicanshu元祖


def collectionpara2(*shoujicanshu,otherparams):
    print("参数的长度是：", len(shoujicanshu),otherparams)
    print("第二个参数是：", shoujicanshu[1],otherparams)    #收集参数与其他参数联合使用时，要为其他参数设置默认参数

collectionpara("胡锦涛",0,1,2,3,4,76)

collectionpara2("胡锦涛",0,1,2,3,4,76,otherparams="其他参数")

collectionpara2("胡锦涛",0,1,2,3,4,76,"其他参数")    #如果不指定默认参数，则会报错



