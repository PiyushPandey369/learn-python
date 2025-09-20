# Array Attributes

import numpy as np

a1=np.arange(11)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print("Elements are:")
print(a1)
print(a2)
print(a3)

# ndim -> gives number of dimension of given array
print("Dimensions:")
print(a1.ndim) 
print(a2.ndim)
print(a3.ndim)

# shape -> tells how many rows and columns in matrix
print("Shapes: ")
print(a1.shape) 
print(a2.shape) 
print(a3.shape) 

# size -> total number of elements in the array
print("Size: ")
print(a1.size)
print(a2.size)
print(a3.size)

# itemsize ->tells memory size occupied

print("Itemsize:")
print(a1.itemsize) #int64 and float occupy same size,, By default it is int64
print(a2.itemsize)
print(a3.itemsize)

# astype -> change datatypes

print("Changing datatype:")
print(a1.astype(np.int8))
print(a2.astype(np.int32))
print(a3.astype(np.float64))
# Immutable


