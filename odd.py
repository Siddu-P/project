num=[]
for n in range(1,21):
    for i in range(0,n):
        if n%2==0:
            break
    else:
        num.append(n)
print(num)