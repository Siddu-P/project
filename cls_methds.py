'''
three methods
Instance methods-- use instance variables--ACCESSORS and MUTATORS
Class methods--use class variables
Static methods--no use of both
'''
class student:
    school='telsko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #ACCESSORS--gets the value
    def get_m1(self):
        return self.m1

    #MUTATORS--sets the value
    def set_m1(self,value):
        self.m1=value

    @classmethod
    def get_school(cls):
        return cls.school
        
    @staticmethod
    def info():
        print('this is a class bro..')

a=student(23,21,24)
student.school='telusko raa'
b=student(34,35,74)
b.set_m1(b.m1+2)
print(b.get_m1())
print(a.avg(),b.avg(),student.get_school())
student.info()