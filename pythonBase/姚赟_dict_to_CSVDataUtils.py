import csv
import json

data = [
{
	"name" : "zhangsan",
	"age" : "15",
	"sex" : "male"
},{
	"name" : "zhang",
	"age" : "16",
	"sex" : "male"
},{
	"name" : "san",
	"age" : "17",
	"sex" : "female"
},{
	"name" : "zhangone",
	"age" : "18",
	"sex" : "female"
}];



def transferData(data):
       json_str= json.dumps(data);
       return json.loads(json_str);


def process(datas):
    index = 0;
    titleList = [];

    resultList = [];
    for result in datas:
        valueList = [];
        for key,value in result.items():

            if(index == 0):
                titleList.append(key);
            valueList.append(value);
        resultList.append(valueList);
        index = index + 1

    print(titleList)
    print(resultList)


#http: // blog.csdn.net / waple_0820 / article / details / 70049953
if __name__ == '__main__':
   newData = transferData(data)
  # print(newData)#
   process(newData)