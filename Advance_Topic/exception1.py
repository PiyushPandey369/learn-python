'''
    try-except Example
    
'''
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    val=num1/num2
    print(val)
    
except ValueError as v:
    print("Invalid Input :",v)
    
except Exception as e:
    print(e)