import numpy as np


a1 = np.arange(10)                       # 1D array
a2 = np.arange(12).reshape(3, 4)         # 2D array (3x4)
a3 = np.arange(27).reshape(3, 3, 3)      # 3D array (3x3x3)

# np.nditer() is efficient way to iterate an array

print("Printing 1D")
for i in a1:
    print(i)

print("Or:")
for i in np.nditer(a1):
    print(i)

print("Printing 2D")
for i in a2:
    for j in i:
        print(j)
print("Or:")
for i in np.nditer(a2):
    print(i)      
    
print("Printing 3D")   
for i in a3:
    for j in i:
        for k in j:
            print(k)
print("Or:")
for i in np.nditer(a3):
    print(i)