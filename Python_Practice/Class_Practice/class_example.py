'''
    class example
    
'''
class Person:
    name="Piyush"
    age=21
    
p2=list()
p1=Person()
print(p2)
# When we use print(), __str() is called itself. (In built-in class __str() is defined but in user_defined __str is not defined )
#  So different behavior

print(f"Name:{p1.name} and Age: {p1.age}")
p1.name="Rahul"
print(f"Name:{p1.name} and Age: {p1.age}")