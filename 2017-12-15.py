


#费波那锲数列

# num=int(input("请输入数列的个数："))
# n1=0
# n2=1
# counter=2
# if num<0:
#     print("输入值不合法")
# elif num==1:
#     print(n1)
# else:
#     print("费波纳数列")
#     print(n1,',',n2,end=',')
#     while num>counter:
#         nth=n1+n2
#         print(nth,end=',')
#         n1=n2
#         n2=nth
#         counter+=1


#用迭代器实现阿姆斯特朗数

import sys
num=int(input("input a num >0: "))

if num<0:
    print("num count<0")

n=len(str(num))

list=list(str(num))

it=iter(list)
while True:
    try:
        sum+=int(next(it))**n
    except expression as identifier:
        if num==sum:
            print("num is 阿姆斯特朗数"%num)
        sys.exit()
