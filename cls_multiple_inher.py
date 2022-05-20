#multiple inheritance
class A:
    def feature1(self):
        print('feature 1 is done')
    def feature2(self):
        print('feature 2 is done')
    
class B():
    def feature3(self):
        print('feature 3 is done')
    def feature4(self):
        print('feature 4 is done') 
class C(A,B):
    def feature5(self):
        print('feature 5 is done')
a1=A()
a2=B()
a3=C()
a1.feature1()
a2.feature3()
a3.feature2()