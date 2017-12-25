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

#      这段代码python3没有此<>这一语法，适用于python2
# if(a<>b):
#     print('Line 3-a is equal to',b)
# else:
#     print("Line 3-a is equal to",b)
if(a<b):
    print("Line 4-a is less than",b)
else:
    print("Line 4-a is not less than",b)
if(a>b):
    print("Line 5-a is greater than",b)
else:
    print("Line 5-a is not greater than",b)

a=5
b=20
if(a<=b):
    print("Line 6 -a is either less than or equal to",b)
else:
    print("Line 6 -a is either less than nor equal to",b)
if(b>=a):
    print("Line 7 -b is either greater than or equal to ",b)
else:
    print("Line 7 -b is either greater than nor equal to ",b)
  

#逻辑运算符
'''
and:布尔与，如果a为false，a and b 返回false。否则返回b的计算值
or：或。如果a是true，返回true，否则它返回y的计算值
not：非，取反！
'''
a=10
b=20
c=0
if(a and b):
    print("Line 1-a and b are true")
else:
    print("Line 1-Either a is not true or b is not true")


#成员运算符
'''
in：如果在指定的序列中找到值返回True，否则返回false
not in：如果在质地昂的序列中没有找到返回值返回true，否则返回false
'''
a=10
b=20
list=[1,2,3,4,5]
if(a in list):
    print("true")
else:
    print("false")
if(b not in list):
    print("True")
else:
    print("false")

a=2
if(a in list):
    print("true")
else:
    print("False")

#身份运算符
'''
is:is是判断两个标识符是不是引用自一个对象  x is y 如果id(x)等于id(y) ，is返回结果1
is not是判断两个标识符是不是引自不同对象  ，反之
'''
a=20
b=20
if(a is b):
    print("line 1-a and b hava same identity")
else:
    print("line 1 -a and b do not have same identity")

if(id(a)==id(b)):
    print("line 2 -a and b have same identity")
else:
    print("line 2-a and b do not hava same identity")

b=30
if(a is b):
    print("line3 -a and b have sanme identity")
else:
    print("line3 -a and b do not have sanme identity")

if(a is not b):
    print("line4 -a and b do not have sanme identity")
else:
    print("line4 -a and b have sanme identity")


#运算符优先级
'''
**   指数（最高优先级）
~ + - 按位翻转，一元加号和减号（最后两个的方法名为+@和-@）
*/%// 乘 除 取模和取整除
+ - 加法减法
>>  << 右移，左移运算符
&  位AND
^  位运算符
<=  <>  >=  比较运算符
<> == != 等于运算符
is is not：身份运算符
in not in 成员运算符
not or and 逻辑运算符

'''

a=10
b=20
c=15
d=5
e=0

e=(a+b) * c/d  
print("value of (a+b) * c/d is",e)


