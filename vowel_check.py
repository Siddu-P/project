'''
string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
'''
'''
string1='abcdeioyu'
vowels='aeiou'
string11=string1.lower
count={}.fromkeys(vowels,0)
for i in string1:
    if i in count:
        count[i]+=1
print(count)
'''
s=input()
s1=s.lower()
v=0
c=0
l=['a','e','i','o','u']
for i in s1:
    if i in l:
        v+=1
    else:
        c+=1
print(f'vow are {v}')
print(f'con are {c}')
