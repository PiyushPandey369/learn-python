# Here are set functions
# np.union1d() ->  gives union of two set
# np.intersect1d() -> gives common elements
# np.setdiff1d() ->present in one set, not available in another set
# np.setxor1d() -> removes the intersection part(common part)
# np.in1d() or np.isin()-> check if element is present in given set or not

import numpy as np

arr1 = np.random.randint(1, 5, size=5)
arr2 = np.random.randint(1, 5, size=5)

# Display the input arrays
print("Array 1:", arr1)
print("Array 2:", arr2)

# --- Set operations ---
print("\n--- Set Operations ---")
print("Union:", np.union1d(arr1, arr2))          # All unique elements from both
print("Difference (arr1 - arr2):", np.setdiff1d(arr1, arr2))  # In arr1 but not in arr2
print("Intersection:", np.intersect1d(arr1, arr2)) # Common elements
print("Symmetric Difference:", np.setxor1d(arr1, arr2))  # Elements in arr1 or arr2, but not both

# --- Membership test ---
print("\n--- Membership Test ---")
print("Is element == 3?:", np.isin(arr1, 3))     # Check if elements of arr1 equal 3