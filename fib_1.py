'''
nterms=int(input("how many terms: "))
num=[]
a,b=0,1
count=0
if nterms<0:
    print("enter positive number")
elif nterms==0:
    num.append(a)
    
elif nterms==1:
    num.append(b)
else:
    print("fib seq:")
    while count<nterms:
        num.append(a)       
        c=a+b
        a=b
        b=c       
        count+=1
print(num)
'''
nt=10
a,b=0,1
c=0
print('fib :')
while c<nt:
    print(a)
    nth=a+b
    a=b
    b=nth
    c+=1
