'''
    Instance vs Class Attribute

    Create a class Car with a class attribute wheels = 4.

    Create two objects of the class.

    Change wheels through one object (obj1.wheels = 6).

    Check if it affects the other object and the class.

    Concept: Difference between class attribute and instance attribute.
'''

class Car:
    wheels=4
c1=Car()
c2=Car()
c1.wheels=6 #aafno ma change vaisakyo,,,change in Car doesnt affect it.(Independent of Car)
print(c1.wheels,c2.wheels)  #No it don't affect
Car.wheels=8
print(c1.wheels,c2.wheels)
