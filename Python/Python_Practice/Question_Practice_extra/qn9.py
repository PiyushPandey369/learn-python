'''
    Write a program to print the shape of a matrix.
'''

n=int(input("Enter the size of matrix:"))

l1=[]

for i in range(1,n+1):
    l2=[]
    for j in range(1,n+1):
        element=int(input(f"Enter the element {i}{j}: "))
        l2.append(element)
    l1.append(l2)
for i in l1:
    print(i)
    
