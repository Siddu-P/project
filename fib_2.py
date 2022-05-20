n=int(input("enter num:"))
fib=[]
a,b=0,1
if n<=0:
    print("enter a positive num")
elif n==1:
    fib.append(a)
    print(fib)
else:
    print("fibonacci sequence:",end="")
    for i in range(0,n):
        fib.append(a)
        c=a+b
        a=b
        b=c
    print(fib,i+1)
