def f (n):
    a = 1
    for i in range(1,n+1):
        a*=i

    return a 

print(f(5))
print(f(1000))