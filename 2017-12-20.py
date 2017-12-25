
#生成器的作用和

import sys
def fibonacci(n,w=0): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        sys.exit()



#不使用yield
# def fibonacci(n,w=0): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         #yield a
#         a, b = b, a + b
#         print('%d,%d' % (a,b))
#         counter += 1
# f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print (next(f), end=" ")
#     except :
#         sys.exit()
