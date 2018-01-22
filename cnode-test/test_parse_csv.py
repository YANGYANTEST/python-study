import csv

def getDataFromCsv():
    all_test_data = []
    with open('./test_data.csv') as filedata:
        #print(filedata)
        #解析数据
        filereader = csv.reader(filedata)
        # print(filereader)

        next(filereader)   # 去掉第一行数据 ['username', 'passwd', 'repasswd', 'email']
        #迭代循环
        for row in filereader:
            #print(row)
            all_test_data.append(row) 

    return all_test_data


data = getDataFromCsv()
print(data)