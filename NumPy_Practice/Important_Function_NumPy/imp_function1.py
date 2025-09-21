import numpy as np
# np.sort() -> return a sorted copy of an array
# np.append() -> append values along the mentioned axis at the end of the array
# np.concatenate() -> concatenate a sequence of array along an existing arrays
# np.unique() -> get unique values from an array

# --- 1. np.sort() ---
# Returns a sorted copy of an array
a = np.random.randint(1, 50, 10)
print("Original a:", a)
print("Sorted ascending:", np.sort(a))          # new sorted array
print("Sorted descending:", np.sort(a)[::-1])   # reverse order
print()

# --- 2. np.append() ---
# Appends values at the end (always returns a new array)
print("Append single value:", np.append(a, 100))
print("Append multiple values:", np.append(a, [101, 102]))
print()

# --- 3. np.concatenate() ---
# Concatenate two arrays
a1 = np.random.randint(1, 50, 10)
a2 = np.random.randint(1, 50, 10)
print("a1:", a1)
print("a2:", a2)
print("Concatenate 1D:", np.concatenate((a1, a2)))
print()

# 2D concatenation
a1 = np.random.randint(1, 50, 10).reshape(5, 2)
a2 = np.random.randint(1, 50, 10).reshape(5, 2)
print("a1:\n", a1)
print("a2:\n", a2)
print("Concatenate row-wise:\n", np.concatenate((a1, a2), axis=0))
print("Concatenate column-wise:\n", np.concatenate((a1, a2), axis=1))
print()

# --- 4. np.sort() in 2D ---
b = np.random.randint(1, 100, 10).reshape(2, 5)
print("b:\n", b)
print("Sort along axis=0 (column-wise):\n", np.sort(b, axis=0))
print("Sort along axis=1 (row-wise):\n", np.sort(b, axis=1))
print()

# --- 5. np.append() in 2D ---
b = np.append(b, np.ones((b.shape[0], 1)), axis=1)   # add a column of 1s
print("After appending a column:\n", b)
print()

# --- 6. np.unique() ---
c = np.array([1, 2, 2, 2, 1, 1, 3, 4, 5, 4, 3, 5])
d = np.array([[1, 2, 1, 2],
              [2, 3, 3, 4]])
print("Unique values in 1D c:", np.unique(c))
print("Unique values in 2D d:", np.unique(d))
