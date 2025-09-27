import pandas as pd
import numpy as np
# size -> gives total items (values) including missing values
# dtype -> series ko value ko datatype
# name -> series object ko name
# is_unique -> items repeat navaye True dinxa
# values -> sabai values extract garxa in the form of numpy array


# ==========================================
# Create a Pandas Series for cricket runs
# ==========================================
runs_list = [3, 67, 5, 33, 80, 110, 0, 145, 0]
runs_series = pd.Series(runs_list, name="Runs Scored")

# ==========================================
# Display the Series
# ==========================================
print("=== Runs Series ===")
print(runs_series)

# ==========================================
# Series Attributes and Methods
# ==========================================
print("\n--- Series Properties ---")
print("Total items (size):", runs_series.size)
print("Data type (dtype):", runs_series.dtype)
print("Series name:", runs_series.name)
print("Is unique?:", runs_series.is_unique)

# ==========================================
# Extract underlying NumPy array
# ==========================================
print("\n--- NumPy Array View ---")
print("Values as NumPy array:", runs_series.values)
print("Type of values:", type(runs_series.values))
print("6th element (index 5):", runs_series.values[5])

