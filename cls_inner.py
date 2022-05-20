class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop('hp','i5',5)
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    
    class laptop:
        def __init__(self,brand,cpu,ram):
            '''
            self.brand='hp'
            self.cpu='i5'
            self.ram=8
            '''
            self.brand=brand
            self.cpu=cpu
            self.ram=ram
        def show(self):
            print(self.brand,self.cpu,self.ram)
    #s1=laptop('hp','i5',5)

s1=student('dsa',4)
s2=student('afsa',5)
#print(s1.name,s1.rollno)
s1.lap.ram=7
s1.show()
#s2.show()
