''' 
    Constructors (__init__)

    Create a class Student with attributes name and marks. Initialize them using a constructor and 
    write a method to display the details.

    Concept: How __init__ assigns values to each object.

'''

class Student:
    name=""
    marks=0
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def display(self):
        print(f"Name: {self.name} Marks: {self.marks}")


s1=Student("Piyush",98.0)
s1.display()

