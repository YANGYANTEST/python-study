#while判断条件 

#用while计算1到100的总和：
#方法1：
num=100
sum=0

counter=1
while counter<=num:
    sum=sum+counter
    counter +=1
print("1 到 %d 之和为：%d"%(num,sum))


#无限循环
# var=1
# while var==1:
#     num=int(input("输入一个数字："))
#     print("你输入的数字是：",num)
# print("Good bye!")


#while 循环使用else语句 
count=0
while count<5:
    print(count,'小于5')
    count=count+1
else:
    print(count,"大于或等于5")


#for循环
languages=['C','c++','java','python','nodejs']

for x in languages:
    print(x)

print("============================")

#使用break、continue 跳出循环conti
#break：跳出整个循环，终止循环语句,相当于急刹车
#continue:跳出当前循环，然后继续进行下一轮循环。
sites=['baidu','Google','Taobao','Tianmao']
for s in sites:
    if s=='Taobao':
        print('淘宝')
        break
    print('循环数据: '+s)
else:
    print("没有循环数据")

print("完成循环")

print('=========================')

#range()函数，生成数列
for i in range(1,10):   #包左不包右
    print(i)

print("============================")

#还可以设置步长
for i in range(0,100,2):
    print(i)

print("=================================")

#结合range()和len()函数 返回一个序列的索引

a=['baidu','guge','taobao','qq']
for i in range(len(a)):
    print(i,a[i])


print("====================================")



#对比brea and continue

for letter in 'Taobao':
    if letter =='b':
        break
        # continue
    print("当前字母为：",letter)

print("================================")

var=10
while var>0:
    print('当前变量值为：',var)
    var=var-1
    if var==4:
        break
        # continue
print('Byebye')

print("=======================")

for n in range(2,10):
    for x in range(2,n):
        if n % x==0:
            print(n,'=',x,'*',n//x)
    else:
        #循环中没有找到元素
        print(n,' 是质数')

print("============================")


#pass语句块：
for letter in 'Taobao':
    if letter=='b':
        pass
        print('执行pass模块')
    print('当前字母：',letter)



#作业
'''
阿姆斯特朗数，如果一个n位正整数等于各位数字n次方的和，我们称该数为阿姆斯特朗数，
如：1*3+5*3+3*3=153，那么153就是阿姆斯特朗数。
1000以内的阿姆斯特朗数有：1,2,3,4,5,6,7,8,9，153,370，371,407
写一个程序检测输入的数是否是阿姆斯特朗数
'''






