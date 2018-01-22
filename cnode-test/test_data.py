
import time
from selenium import webdriver



test_data=[
    ['xiaoming','123456','123456','xm@1234.com'],
    ['','123456','123456','xm@1234.com'],
    ['xiaoming','','123456','xm@1234.com'],
    ['xiaoming','123456','','xm@1234.com']
]

test1_data=['xiaoming','123456','123456','xm@1234.com']

#思路：循坏嵌套，先循环拿出每一行的数据，再拿出每行的单个数据
for x in range(len(test_data)):
    print(x,"===>",test_data[x])
    for y in range(len(test_data[x])):
        print(x,":",y,"===>",test_data[x][y])

