'''
字符串的操作
%s:代表字符串
%d:数字（整形）
%f:打印浮点数，
%.2f:保留几位小数
'''
name="xiaoming"
address="china"
age=18
money=100.126

print(name,address)

print(name+" "+address)

#作业：修改以上数据，能够打出浮点数字，如100.126
print("my name is %s,i live in %s,i am %d years old,i have %d money"%(name,address,age,money))

print("his money is %f"%(100.126))#打印浮点数
print("i have %.3f money"%(100.12634))#打印浮点数（指定保留小数点位数）

print ("His height is %f m"%(1.83))


print(name * 2)
