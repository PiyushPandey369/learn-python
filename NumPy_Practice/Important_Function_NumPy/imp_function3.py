# np.histogram() ->counts how many values fall into bins(interval) that is defined
# np.corrcoef() ->tells how strongly two(or more) datasets are linearly related
# np.isin() ->items are checked in array
# np.flip() -> reverses the order of array
# np.put() -> change multiple items in array (permanent change)
# np.delete() -> returns a new array with the deletion of sub-arrays along with the mentioned axis

import numpy as np

# --- Random data for histogram ---
data = np.random.randint(1, 100, size=20)   # 20 random numbers between 1 and 99
print("Data:", data)

# Histogram with defined bins
hist, bin_edges = np.histogram(data, bins=[0,10,20,30,40,50,60,70,80,90,100])
print("\n--- Histogram ---")
print("Counts:", hist)
print("Bin edges:", bin_edges)

# --- Correlation Example ---
salary = np.array([20000, 40000, 25000, 35000, 60000])
experience = np.array([1, 3, 2, 4, 2])

print("\n--- Correlation Coefficient ---")
print(np.corrcoef(salary, experience))

# --- Membership Test ---
print("\n--- Membership Test ---")
print("Is element == 10?:", np.isin(data, 10))
print("Is element in [10,20,30,40]?:", np.isin(data, [10, 20, 30, 40]))

# --- 2D Array Flipping ---
matrix = np.random.randint(1, 50, size=10).reshape(2, 5)
print("\nMatrix:\n", matrix)

print("\n--- Flipping Operations ---")
print("Flip all elements:", np.flip(matrix))
print("Flip row order (axis=0):\n", np.flip(matrix, axis=0))
print("Flip 1D array 'data':", np.flip(data))

# --- Modify Array Elements ---
np.put(data, [0, 1], [110, 111])   # Replace elements at indices 0 and 1
print("\n--- Modify Elements ---")
print("After np.put:", data)

print("Delete index 5:", np.delete(data, 5))
print("Delete indices [7, 9]:", np.delete(data, [7, 9]))

# --- Clipping ---
print("\n--- Clipping ---")
print("Clip data to [30, 80]:", np.clip(data, a_min=30, a_max=80))