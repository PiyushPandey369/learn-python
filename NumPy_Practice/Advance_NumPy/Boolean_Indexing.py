import numpy as np

# --- Array Creation ---
a = np.arange(24).reshape(6, 4)
print("Original Array (6x4):\n", a)

# --- Boolean Indexing Examples ---

# 1. All elements greater than 5
print("\nElements greater than 5:\n", a[a > 5])

# 2. All elements greater than 5 AND even
print("\nElements greater than 5 and even:\n", a[(a > 5) & (a % 2 == 0)])

# 3. All odd elements (NOT even)
print("\nOdd elements (a % 2 != 0):\n", a[~(a % 2 == 0)])
