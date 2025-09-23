'''
     
    Instance Method, Class Method, Static Method

    Create a class Maths:

    An instance method that prints a number.

    A class method that changes a class-level variable.

    A static method that prints a motivational message.

    Concept: Difference between instance methods, class methods, and static methods.

'''
class Maths:
    
    def instance_method(self,x,y):
        print(f"{x},{y}")
        
    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class is: {cls.__name__}")
        
    @staticmethod
    def static_method():
        print("Life goes on,,, Don't get stuck")

m = Maths()
m.instance_method(5, 7)   # Instance method (object needed)
m.class_method()          # Class method (can be called with object)
Maths.class_method()      # Class method (can also be called with class)
m.static_method()         # Static method
Maths.static_method()     # Static method


