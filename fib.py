def fib(n):
    num=[]
    a,b=0,1
    if n<=0:
        print("enter positive number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
        num.append(c)
    print(num)
    
fib(10)
    



