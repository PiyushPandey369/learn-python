# NumPy array vs Python Lists
# 1)Speed
# 2)Memory
import numpy as np
import time
import sys

print("Speed Check")
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
start=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])
t=time.time()-start
print(t)

a1=np.arange(10000000,dtype=np.int8)
b1=np.arange(10000000,20000000)
start1=time.time()
c1=a1+b1
t1=time.time()-start1
print(t1)
print(f"NumPy array is {(t)/(t1)} faster than Python List")


print("Memory check")
print("List Size: ",sys.getsizeof(a))
print("NumPy Array Size: ",sys.getsizeof(a1))
