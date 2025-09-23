'''
   Map-Filter-Reduce in Python
   
'''

from functools import reduce
l=[1,2,34,6.7,7]

sq=lambda x:x*x

sq1=list(map(sq,l))
print(sq1)


def check_num(num):
    if(num%2!=0):
        return True
    return False

sq2=list(filter(check_num,sq1))
print(sq2)

def sum(a,b):
    return a+b

sq3=reduce(sum,l)
print(type(sq3))
print(sq3)