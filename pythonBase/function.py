def firstfunction(name):
    "函数文档，函数的_doc_"
    print("形参是name" + "实参是" + name )


firstfunction.__doc__

help(firstfunction)

def function_return(a,b):
    s = a + b
    return s

print (function_return(1,1))

print.__doc__

