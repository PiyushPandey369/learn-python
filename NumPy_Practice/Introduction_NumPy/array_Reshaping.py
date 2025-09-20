import numpy as np

# reshaping includes:
# reshape() -> defn dimensions
# transpose() -> interchanges rows and columns
# raval() -> convert any dimension into 1D

a2 = np.arange(12).reshape(3, 4)         # 2D array (3x4)

print(a2)

print("Transposing:")
print(np.transpose(a2))
print("Or:")
print(a2.T)

print("Raval:")
print(a2.ravel())