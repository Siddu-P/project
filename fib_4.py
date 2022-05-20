'''
def fib(n):
    a=0
    b=1
    for i in range(0,n):
        print(a)
        a,b = b,a+b
fib(10)
'''
def fib(n):
    a,b=0,1
    for i in range(0,n):
        print(a)
        a,b=b,a+b
fib(10)