#if条件循环
var1=100
if var1:
    print("1 - if 表达式条件为 True")
    print(var1)
else:
    print('NONO')

var2=0
if var2:
    print('2 - if 表达式条件为 true')
    print(var2)
print('Byebye')



#if....else...

age=int(input("请输入你的年龄："))
print("")
if age<0:
    print("我才不信呢")
elif  age==1:
    print("小屁孩")
elif age==2:
    print("大屁孩哈")
elif age>2:
    human=22+(age-2)*5

    print("真实年龄为：",human)
else:
    print("好好反省一下")

input('点击enter键退出')


#数字猜谜游戏
number=7
guess=-1
print("数字猜谜游戏@")
while guess !=number:
    guess=int(input("请输入你猜的数字："))

    if guess==number:
        print("恭喜你猜对啦！")
    elif guess<number:
        print("猜小啦")
    elif guess>number:
        print("大咯~~~~")


#if..elif ...else ...语句嵌套

num=int(input("请输入一个数字："))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字，可以被2整除；但不能整除3")
else:
    if num%3==0:
        print("你的数字可以3整除，不能被2整除")
    else:
        print("2 and 3 都不能被整除~~~")
        
