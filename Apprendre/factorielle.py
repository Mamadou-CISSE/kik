def fac(n):
    return 1 if n == 0 else n * fac(n-1)

def fac1(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

print(fac1(3))