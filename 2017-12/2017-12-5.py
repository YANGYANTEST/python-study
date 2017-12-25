

#元祖 tuple
tup="a","b","c"
print(tup)

#访问元素
tup1=('physics','chemistey',1997,2000)
tup2=(1,2,3,4,5,6)
print("tup1[0]:",tup1[0])
print("tup2[1:5]:",tup2[1:5])

#修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
#tup1[0]=100    #报错，因为元素值是不允许修改的
#print(tup1)

#创建一个新的元素
tup3=tup1+tup2
print(tup3)


#元祖运算符
a=1,2,3,4
b=356,233,556
print(len(a))
print(a+b)
print(("Hi")*4)
print(3 in (1,3,6,7))

#截取，索引
a=('spam', 'Spam', 'SPAM!')
print(a[2])
print(a[-1])
print(a[1:])

#思考：list和tuple的相同点和不同点
'''
相同点:
1.都是序列数据类型
2.容器里面的元素都是有索引概念
3.迭代（对象）-----for item in 对象：此时的对象就是可迭代的
4.元素的类型可以不相同
5.都支持负索引
6.支持切片
7.获取元素的速度接近一个恒定值

不同点：
list-----定义之后还可以改变；tuple定义好之后里面的元素不可改变

'''

