n=5
m=97
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(m)
        print(ch, end='')
        m+=1
    print()