'''
    Write a program to find the maximum of the numbers in a list using the reduce 
    function.
'''

from functools import reduce

l=[5,6,70,90,1,10,25,4]


def check_max(num1,num2):
   if( num1<num2):
       num1=num2
   return num1
    
res=reduce(check_max,l)
print(res)