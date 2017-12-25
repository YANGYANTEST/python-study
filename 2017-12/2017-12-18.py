#如何将数据写入csv文件

import csv
with open("date/data.csv",mode='w')as f:
    w=csv.writer(f)
    w.writerow(['1','3','2'])
f.close()