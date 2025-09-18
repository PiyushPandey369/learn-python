'''
    Write a list comprehension to print a list which contains the multiplication table of a 
    user entered number.
'''

n=int(input("Enter the number: "))
l1=[]
l=[n*i for i in range(0,11)]
print(l)