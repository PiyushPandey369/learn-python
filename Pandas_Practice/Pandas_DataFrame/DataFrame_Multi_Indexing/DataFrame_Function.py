import pandas as pd
import numpy as np

# --------------------------------------------------
# Create MultiIndex for rows (branch, year)
# --------------------------------------------------
index_val1 = pd.MultiIndex.from_product(
    [['cse', 'ece'], [2019, 2020, 2021, 2022]]
)

# Create DataFrame with MultiIndex in rows & columns
branch_df2 = pd.DataFrame(
    [
        [1, 2, 0, 1],
        [3, 4, 0, 1],
        [5, 6, 0, 1],
        [6, 7, 0, 1],
        [7, 8, 0, 1],
        [9, 10, 1, 2],
        [15, 60, 3, 1],
        [61, 71, 5, 6]
    ],
    index=index_val1,
    columns=pd.MultiIndex.from_product(
        [['Kathmandu', 'Pokhara'], ['Avg_Package', 'Students']]
    )
)

# --------------------------------------------------
# Display full DataFrame
# --------------------------------------------------
print("Full MultiIndex DataFrame:\n", branch_df2)


# --------------------------------------------------
# Common DataFrame operations
# --------------------------------------------------

# Show first 5 rows
print("\nHead (first 5 rows):\n", branch_df2.head())

# Show last 5 rows
print("\nTail (last 5 rows):\n", branch_df2.tail())

# Display DataFrame info (index, dtypes, memory usage)
print("\nInfo about DataFrame:")
print(branch_df2.info())

# Check for duplicated rows
print("\nCheck duplicated rows:\n", branch_df2.duplicated())

# Check for missing values (NaN)
print("\nCheck for NaN values:\n", branch_df2.isna())

# --------------------------------------------------
# Sorting with MultiIndex
# --------------------------------------------------

# Sort by full MultiIndex → (branch descending, year ascending)
print("\nSort by full MultiIndex (branch ↓, year ↑):\n",
      branch_df2.sort_index(ascending=[False, True]))

# Sort only by 2nd level (year) in descending order
print("\nSort by 'year' level (descending):\n",
      branch_df2.sort_index(level=1, ascending=[False]))

# --------------------------------------------------
# Reshaping
# --------------------------------------------------

# Transpose DataFrame (swap rows and columns)
print("\nTranspose DataFrame:\n", branch_df2.transpose())

# Swap levels of MultiIndex in rows (branch ↔ year)
print("\nSwap MultiIndex levels (branch ↔ year):\n", branch_df2.swaplevel())


