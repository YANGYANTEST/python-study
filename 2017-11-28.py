#运算付和操作对象

'''
算数运算符：
以下假设变量a为10，变量b为20
运算符           描述                                         实例
+               加-两个对象相加                             a+b输出结果30
-               减-得到负数或是一个数减去另一个数             a-b的输出结果-10
*               乘*两个数相乘或是返回一个被重复若开次的字符串  a*b输出结果为2004
/                除 - x以为y                                b/a 输出结果2
%               取模---返回除法的余数                        b%a输出结果为
**              幂-返回x的y次幂                              a**b 为的10的20次方
//              取整除-返回商的整数部分                        9//2输出4，9.0//2.00为4.0
'''

#作业：
a=21
b=10
c=0
c=a+b
print("Line 1-vlaue of c is ",c)

c=a-b
print("Line 2-value of c is ",c  )

c=a*b
print("Line 3-value of c is",c )

c=a/b 
print("Line 4-value of c is",c)

c=a%b 
print("Line 5-value of c is",c)

a=2
b=3
c=a**b 
print("line 6-value of c is",c)

a=10
b=5
c=a//b 
print("line 7-value of c is",c)


#python比较运算符
a=21
b=10
c=0
if(a==b):
    print("Line 1-a is equal to",b )
else:
    print("Line 1-a is not equal to", b)

if(a!=b):
    print("Line 2-a is equal to",b )
else:
    print("Line 2-a is not equal to", b)
if( a<>b):
    print('Line 3-a is equal to',b)
else:
    print("Line 3-a is equal to",b)