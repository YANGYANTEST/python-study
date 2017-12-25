

#用函数的方式将数列写入到csv文件中

import csv

x=int(input("请输入一个数字："))
def feibo(num):
    n1,n2=0,1
    list=[n1,n2]
    nth=0
    for i in range(0,x):
        nth=n1+n2
        if nth<=num:
            n1=n2
            n2=nth
            list.append(nth)
    # print(list)
    return list
# feibo(x)
def weite_csv(list):
    with open("date/data.csv",mode='w')as f:
        w=csv.writer(f)
        w.writerow(list)
    f.close()

list=feibo(x)
weite_csv(list)