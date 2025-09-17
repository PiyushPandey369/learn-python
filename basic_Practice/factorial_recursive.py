'''
    Write a function factorial_recursive(n) 
    to calculate factorial using recursion.
    
'''

def factorial_recursive(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial_recursive(num-1)

num=int(input("Enter the number to find factorial:"))
result=factorial_recursive(num)
print(f"The result is {result}")