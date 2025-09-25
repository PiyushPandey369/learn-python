# Fancy Indexing is used when there is no proper pattern in output
import numpy as np

# --- Array Creation ---
a = np.arange(24).reshape(6, 4)
print("Original Array (6x4):\n", a)

# --- Fancy Indexing Examples ---

# 1. Select 1st, 3rd, and 4th row (rows 0, 2, 3 by index)
print(a[[0, 2, 3]])

# 2. Select all rows, but only columns 0, 2, and 3
print(a[:, [0, 2, 3]])

# 3. Select rows 1, 3, 4 and all columns starting from index 1
print(a[[1, 3, 4], 1:])

# 4. Select rows 3, 4, 5 and columns with step = 3 (i.e., col 0 and col 3)
print(a[[3, 4, 5], 0:4:3])

