# The isinstance() method is used to check the relationship between the objects and classes. It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.


class Calculation1:  
    def Summation(self,a,b):  
        return a+b

class Calculation2(Calculation1):  
    def Multiplication(self,a,b):  
        return a*b

class Derived(Calculation2):  
    def Divide(self,a,b):  
        return a/b
c1 = Calculation1()
c2 = Calculation2()
d = Derived()  

print(isinstance(c1,Derived))
print(isinstance(c1,Calculation2))
print(isinstance(c1,Calculation1))

print(isinstance(c2,Derived))
print(isinstance(c2,Calculation2))
print(isinstance(c2,Calculation1))

print(isinstance(d,Derived))
print(isinstance(d,Calculation2))
print(isinstance(d,Calculation1))