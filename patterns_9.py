n=int(input("enter a num:"))
num=97
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()

"""
# Python code 3.x to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def contalpha(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
- for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# explicitely converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
		
			# incrementing at each column
			num = num +1
	
	
		# ending line after each row
		print("\r")

# Driver code
n = 5
contalpha(n)

"""