#解析CSV文件存储数据到列表

#getcwd():查看当前的路径

import os
import csv
# print(os.getcwd())

#get csv file path:获取csv的路径
filepath=os.path.join(os.getcwd(),"date","111.csv")
#print(filepath)

#open csv file
f=open(filepath)

users=[]
#解析数据
reader=csv.reader(f)
print(reader)

for row in reader:
    print(row)
#把第一行数据删除
next(reader,None)

#迭代循环
for row in reader:
    #print(row)
    users.append(users)
print(users)