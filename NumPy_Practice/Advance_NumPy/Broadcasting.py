# Broadcasting
import numpy as np

# 1. Scalar with array
a1 = np.arange(12).reshape(3, 4)
print("a1:\n", a1)
print("\nAdding scalar:\n", a1 + 5)   # scalar broadcasted to all elements

# 2. 1D array with 2D array (row-wise)
a2 = np.array([1, 2, 3, 4])   # shape (4,)
print("\nAdding row vector:\n", a1 + a2)  # broadcasted to each row

# 3. 1D array with 2D array (column-wise)
a3 = np.array([10, 20, 30]).reshape(3, 1)   # shape (3,1)
print("\nAdding column vector:\n", a1 + a3)  # broadcasted to each column

# 4. Different shaped 2D arrays
a4 = np.arange(4).reshape(1, 4)   # shape (1,4)
print("\na4:\n", a4)
print("\na1 + a4:\n", a1 + a4)   # a4 is broadcast to 3 rows

# 5. 3D and 2D broadcasting
a5 = np.arange(8).reshape(2, 4)      # shape (2,4)
a6 = np.arange(24).reshape(2, 3, 4)  # shape (2,3,4)
print("\n3D + 2D:\n", a6 + a5)       # a5 broadcasted to match shape (2,3,4)

# 6. Broadcasting with random integer
a7 = np.random.randint(10)  # scalar
print("\nRandom int added:\n", a1 + a7)

# 7. Mismatched case (error)
try:
    a8 = np.arange(6).reshape(2, 3)  # shape (2,3)
    print(a1 + a8)
except ValueError as e:
    print("\nError example:", e)
