
#元祖，列表：用[]括起来
'''
列表操作包含以下函数:
1、cmp(list1, list2)：比较两个列表的元素 
2、len(list)：列表元素个数 
3、max(list)：返回列表元素最大值 
4、min(list)：返回列表元素最小值 
5、list(seq)：将元组转换为列表 
'''
'''
列表操作包含以下方法:
1、list.append(obj)：在列表末尾添加新的对象
2、list.count(obj)：统计某个元素在列表中出现的次数
3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
5、list.insert(index, obj)：将对象插入列表
6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7、list.remove(obj)：移除列表中某个值的第一个匹配项
8、list.reverse()：反向列表中元素
9、list.sort([func])：对原列表进行排序
'''


list=['Google','baidu',1773]
print(list)

#更新值,没有索引，强制赋值会报错
list[1]=['a','b','c']
print(list)

#删除列表
del list[2]
print(list)

#其他操作
print(len(list))
print('a' in list)

#嵌套列表
a=['a','b','c']
b=[1,2,3]
c=[a,b]
print(c,len(c),c[0],c[0][1])

# a=[1,2,3,4,5,[122,33,44,66,111]]
# print(min(a))

#作业：求出最大值最小值
list2=[1,2,3,45]
list3=[1,2,3,[4,5,6]]
list4=['ww',3,5]
print("min",min(list2),"max",max(list2))
print(min(list3[3]))
print(max(list3[3]))
#print(min(list4),max(list4))#报错

app=['sunday','monday','happy','linda','status']
obj=['真','的','嘛','?']
print(app.append(obj)) #返回为None

#作业：把所有的方法写一遍
yangyan=[1,2,345,6,78,3,44,77,1124,4]
print(yangyan.append(5678))#返回w为None
print(yangyan.count(3))
print(yangyan.insert(1,66))#返回为空

#分片赋值
a=["我爱学习"]
a[1:]="超级爱学习"
print(a)

