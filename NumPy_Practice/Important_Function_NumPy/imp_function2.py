import numpy as np

# np.expand_dims -> we can get the expanded dimensions of an array
# np.where -> returns the indices of elements in an input array where the given condition is satisfied
# np.argmax() -> returns indices of the max element of the array in a particular axis
# np.argmin() -> returns indices of the min element of the array in a particular axis
# np.cumsum() -> used when we want to compute the cumulative sum of array elements over a given axis
# np.cumprod() -> used when we want to compute the cumulative product of array elements over a given axis
# np.percentile() -> Used to compute the nth percentile of the given data


print("===== 1D Array Examples =====\n")

# --- 1D array creation ---
a = np.random.randint(1, 50, 10)
print("Array a:", a, "Shape:", a.shape)

# --- expand_dims ---
b = np.expand_dims(a, axis=1)
print("\nExpanded dims (axis=1):\n", b, "Shape:", b.shape)

# --- where ---
indices = np.where(a > 20)
print("\nIndices where a > 20:", indices)
print("Values where a > 20:", a[indices])
print("Replace values <=20 with 0:", np.where(a > 20, a, 0))

# --- argmax / argmin ---
print("\nIndex of max element:", np.argmax(a), "Value:", a[np.argmax(a)])
print("Index of min element:", np.argmin(a), "Value:", a[np.argmin(a)])

# --- cumulative sum / product ---
print("\nCumulative sum:", np.cumsum(a))
print("Cumulative product:", np.cumprod(a))

# --- percentiles ---
print("\n50th Percentile (Median):", np.percentile(a, 50))
print("25th Percentile (Q1):", np.percentile(a, 25))
print("75th Percentile (Q3):", np.percentile(a, 75))

print("\n===== 2D Array Examples =====\n")

# --- 2D array creation ---
a2 = np.random.randint(1, 50, (3, 4))   # 3 rows, 4 columns
print("2D Array a2:\n", a2)

# --- argmax / argmin ---
print("\nArgmax overall index:", np.argmax(a2))   # flattened index
print("Argmax along axis=0 (per column):", np.argmax(a2, axis=0))
print("Argmax along axis=1 (per row):", np.argmax(a2, axis=1))

print("Argmin along axis=0 (per column):", np.argmin(a2, axis=0))
print("Argmin along axis=1 (per row):", np.argmin(a2, axis=1))

# --- cumulative sum / product ---
print("\nCumulative sum (flattened):", np.cumsum(a2))
print("Cumulative sum along axis=0 (column-wise):\n", np.cumsum(a2, axis=0))
print("Cumulative sum along axis=1 (row-wise):\n", np.cumsum(a2, axis=1))

print("\nCumulative product along axis=0 (column-wise):\n", np.cumprod(a2, axis=0))
print("Cumulative product along axis=1 (row-wise):\n", np.cumprod(a2, axis=1))

# --- percentiles ---
print("\n50th Percentile (overall):", np.percentile(a2, 50))   # median of all values
print("Percentile along axis=0 (per column, Q1=25%):\n", np.percentile(a2, 25, axis=0))
print("Percentile along axis=1 (per row, Q3=75%):\n", np.percentile(a2, 75, axis=1))
