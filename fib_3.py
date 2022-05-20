n=int(input("enter a num:"))
fib=[]
a,b=0,1
count=0
if n<=0:
    print("enter a positive number")
elif n==1:
    fib.append(a)
    print(fib)
else:
    print("fibonaci sequence:",end="")
    while count<n:
        fib.append(a)
        c=a+b
        a=b
        b=c
        count+=1
    print(fib,count)