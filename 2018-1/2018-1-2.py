'''
python基础---递归函数
'''

def f(n):
    if n==1:
        return 1
    return n * f(n-1)

print(f(1))
print(f(3))
print(f(5))