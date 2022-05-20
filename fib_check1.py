import math
def isperfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def isfibonacci(n):
    return isperfectsquare(5*n*n+4) or isperfectsquare(5*n*n-4)
n=int(input("enter a num:"))
if isfibonacci(n)==True:
    print(f"{n} is fibo")
else:
    print(f"{n} is not fibo")