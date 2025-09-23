# Magic Methods

class Fraction:
    
    def __init__(self,n,m):
        self.num=n
        self.den=m
    
    def __str__(self):
        return (f"{self.num}/{self.den}")
    
    def __add__(self,other):
        temp_num=self.num*other.den+self.den*other.num
        temp_den=self.den*other.den
        return(f"{temp_num}/{temp_den}")
    
    def __sub__(self,other):
        temp_num=self.num*other.den-self.den*other.num
        temp_den=self.den*other.den
        return(f"{temp_num}/{temp_den}")
    
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return(f"{temp_num}/{temp_den}")
    
    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return(f"{temp_num}/{temp_den}")
    
x=Fraction(6,5)
y=Fraction(4,3)
# print(type(x))
a=4/3
b=6/5
print(a+b)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)

