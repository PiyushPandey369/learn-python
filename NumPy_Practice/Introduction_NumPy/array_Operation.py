# Array Operation
import numpy as np

a1=np.arange(11)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

# Two types of operation : 
# 1) Scalar

# arithmetic (+,-,*,/,**,%)
print(a1+2)
print(a1*2)
print(a1/2)
print(a1-2)
print(a1**2)

# relational (<,>,==) -> returns true or false
print(a1>2)
print(a1<2)
print(a1==2)

# 2) Vector -> applying operatir on two numpy array (order must be same)
a4=np.arange(10,18).reshape(2,2,2)
#  a3 and a4 are of same order
print(a3+a4)
print(a3-a4)
print(a3*a4)
print(a3/a4)



