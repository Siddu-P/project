'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
print(fact(5))
'''
def fact(n): 
    if n==0:
        return 1
    return n*fact(n-1)
res=fact(5)
print(res)  