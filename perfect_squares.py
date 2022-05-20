def perfect_squares(a,b):
    for i in range(a,b+1):
        if i**(.5)==int(i**(.5)):
            print(i)
a=1
b=10
perfect_squares(a,b)