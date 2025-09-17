'''
    Write a program to print odd element from a list using enumerate 
    function.

'''

l=[1,2,"a",3,'b',123,4,5,6,7,8]

for i,items in enumerate(l):
    if i%2!=0:
        print(i,items)