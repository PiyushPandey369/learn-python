'''
    Example of Custom Exception
    
'''
class Custom_Exception(Exception):
    def __init__(self,message="Something went wrong"):
        super().__init__(message)
        

def check_age(age):
    if age<18:
        # raise Custom_Exception()
        raise Custom_Exception("Invalid Age entered")
    else:
        print("Okay")

age=int(input("Enter the age:"))    
try:
    check_age(age)
except Exception as e:
    print(e)