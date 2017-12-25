#字符串
#访问字符串的值
var="hello world"
var2 = "Runoob"
print("var[0]:",var[0])
print("var2[1:3]:",var2[1:3])

#字符串更新
var="今天是周三啦！"
print(var[:7]+"今晚吃泡面")

#转义符
'''
\\:反斜杠
\b:退格
\e:转义
\n:换行
\r  回车
\f 换页
'''

#运算符
a='hello'
b='python'

print(a+b)
print(a*2)
print(a[2])
print(a[1:4])

if "h" in a:
    print("h在变量中存在")
else:
    print("h不在变量中存在")

if "M(" not in a:
    print("M不再a变量中")
else:
    print("M在变量中")

print(r'\n')
print(R'\n')

#python字符串格式化
print("我叫 %s 今年 %d 岁！"%("杨艳",21))

#字符串格式化符号：
'''
%c 格式化字符及其ASCII码
%s 格式化字符串
%d 格式化整数
%u 无符号整型
%f 浮点数字
%e 格式化浮点数字，可指定小数点后带精度

'''
print("his height is %f m!"%(1.8219))

str="""
这是一个多行字符串，
多行字符串可以使用制表符
TAB（\t）
也可以使用换行符\n
"""
print(str)

#内置函数：
a="helloworld"
print(a.capitalize())#capitalize将字符串带第一个字符转换为大写
print(a.count("l"))#count出现的次数
print(a.center(12,"*"))#center字符串带长度，*号补充
print(a.encode())#转换为编码返回
print(a.endswith('d'))#判断是否为d结尾

info='abcd'
print(info.find('a'))   # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
print(info.find('a',1)) # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
print(info.find('3'))   # 查找不到返回-1

