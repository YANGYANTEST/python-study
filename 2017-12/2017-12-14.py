

#迭代器
'''
是访问集合元素的一种方式
可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束，只能往前不会后退。
有两个基本的方法：iter() 和 next()。
'''

list=[1,24,5,7,'hi']
it=iter(list)        #创建迭代器对象
print(next(it))         #输出迭代器的下一个元素

print("===================================")

a=['hi','ben',1,4,6,'taobao']
it=iter(a)      #创建迭代器对象
for x in it:
    print(x)

print("=================================")

#next()函数
import sys #引入sys模块
list=[1,23,556,77,'tao','bao',13]
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
