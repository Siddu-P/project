'''
n=int(input("enter a num:"))
sum=0
order=len(str(n))
copy_n=n
while n!=0:
    dig=n%10
    sum+=dig ** order
    n=n//10
if sum==copy_n:
    print(f"{copy_n} is an armstrong number")
else:
    print(f"{copy_n} is not an armstrong number")
print(f"sum of given number is {sum}")
'''

n=153
sum=0
order=len(str(n))
temp=n
while temp>0:
    dig=temp%10
    sum+=dig**order
    temp//=10
if n==sum:
    print('yes')
else:
    print('no')


