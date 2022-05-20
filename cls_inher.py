#inheritance
#single level 
class A: #super class(parent)
    def feature1(self):
        print('feature 1 is done')
    def feature2(self):
        print('feature 2 is done')
    
class B(A): #sub class(child class)
    def feature3(self):
        print('feature 3 is done')
    def feature4(self):
        print('feature 4 is done')     
a1=A()
a2=B()
a1.feature1()
a2.feature2()



