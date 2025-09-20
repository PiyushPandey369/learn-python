import numpy as np

# dtype of array() is interger by default
a=np.array([1,2,3])
print(a,a.dtype)

# dtype=float
b=np.array([1,2,3],dtype=float)
print(b,b.dtype)

# np.arange() -> similar to range() [1st included, last excluded]

c=np.arange(1,11)
print(c)
print(np.arange(1,11,2)) #skip second elements

d=np.arange(1,11,dtype=float)
print(d)

# with reshape -> 3 rows 4 columns
e=np.arange(1,13).reshape(3,4)
print(e)