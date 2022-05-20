'''
def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1
        return fact
num=int(input("enter a num:"))
res=factorial(num)
print(f"factorial of {num} is {res}")
'''
def fact(n):
    if n==0:
        return 1
    return (n* fact(n-1))
n=5
res=fact(n)
print(res)