#使用python打印出9 9乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print('{}*{}={}\t'.format(y,x,x*y),end='')
    print()

print("=============================")


for x in range(1,10):
    for y in range(1,x+1):
        print('{}+{}={}\t'.format(y,x,x+y),end='')
    print()


#求10到100中能被3或5整除的数的和
sum=0
for i in range(10,101):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)

print("=================================")


#求从1-100的奇数和
sum=0
for j in range(1,100,2):
    sum+=j
print(sum)

print("==================================")


#随机生成一个手机号码
# (13XXXXXXX,15XXXXXXXX,17XXXXXXXXX,18XXXXXXXXX）
import random

def Create_num():
    list=['13','15','17','18']
    str='0123456789'
    for i in range(10):
        print(random.choice(list)+"".join(random.choice(str)for i in range(8)))

Create_num()



#冒泡排序
arays = [1,18,21,62,3,9,4]
for i in range(len(arays)):
    for j in range(i+1):
        if arays[i] < arays[j]:
            # 实现连个变量的互换 ab=ba
            arays[i],arays[j] = arays[j],arays[i]
print(arays)


