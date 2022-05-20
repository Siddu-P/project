n=int(input("enter a num:"))
f3=0
f1=1
f2=1
if n==0 or n==1:
    print("yes")
else:
    while f3<n:
        f3=f1+f2
        f2=f1
        f1=f3
    if f3==n:
        print("yes")
    else:
        print("no")