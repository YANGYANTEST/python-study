
#字典
student=['xiaoming','zhangsan','lisi']
number=[2001,2002,2003]
print("zhangsan number:",number[student.index('zhangsan')])

student={"zhangsan":2001,"xiaoming":2002,"lisi":2003}
print(student["xiaoming"])

#更新
student["xiaoming"]=2017
print(student["xiaoming"])

#删除
del student["zhangsan"]#删除键“zhangsan”的值
print(student)
student.clear()  # 清空词典所有条目
print(student)
#del student() # 删除词典,此处打印汇报错，因为student字典已被删除，不再存在
#print(student)

#字典的特性
#1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict={"name":"yangyan","age":34,"name":"joy"}
print(dict["name"])

#2.键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
#dic={["name"]:"yangyan","age":22}
#print(dic['name'])#报错TypeError: unhashable type: 'list'

#3.值可以是字典/列表
a={"name":["joy","king"]}
print(a["name"])
a={"name":{"yan","lin"}}
print(a["name"])

#字典的内置函数和方法
#cmp(dict1, dict2) 比较两个字典元素。
dict={"name":"alin","age":56}
dict1={"name":"bin","age":34}
dict2={"name":"yun","age":7}
dict3={"name":"yun","age":56}
# print("Return Value : %d" %  cmp dict,dict1)
# print("Return Value : %d" %  cmp dict,dict2)
# print("Return Value : %d" %  cmp ict,dict3)
print(len(dict1))
print(type(dict))

dict8=dict1.copy()
print(dict8)

# print(dict.has_key("alin"))报错


#	dict.items()以列表返回可遍历的(键, 值) 元组数组
print(dict.items())

#dict.keys()以列表返回一个字典所有的键
print(dict.keys())

#	dict.values()  以列表返回字典中的所有值
print(dict1.values())

#	dict.update(dict2) 把字典dict2的键/值对更新到dict里
e=dict2.update(dict1)
print(e)    #返回为空

#pop(key[,default])
#删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
print(dict.pop("name")) #输出alin

#popitem()随机返回并删除字典中的一对键和值。
print(dict2.popitem())
print(dict2)
