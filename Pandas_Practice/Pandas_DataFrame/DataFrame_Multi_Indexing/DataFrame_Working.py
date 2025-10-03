import pandas as pd
import numpy as np

# --------------------------------------
# Create MultiIndex for rows (branch, year)
# --------------------------------------
index_val1 = pd.MultiIndex.from_product(
    [['cse', 'ece'], [2019, 2020, 2021, 2022]]
)

# Create DataFrame with MultiIndex in both rows & columns
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

# Display the full DataFrame
print("Full MultiIndex DataFrame:\n", branch_df2)


# --------------------------------------
# Extracting rows
# --------------------------------------

# Extract all rows for branch = 'cse'
# print(branch_df2.loc['cse'])

# Extract a single row (branch = 'cse', year = 2020)
# print(branch_df2.loc[('cse', 2020)])

# Extract multiple rows using slicing (step = 3)
# print(branch_df2.loc[('cse', 2020):('ece', 2020):3])

# Using iloc (row index positions)
# print(branch_df2.iloc[1:5:3])        # rows at positions 1 and 4
# print(branch_df2.iloc[[1, 6, 7]])    # specific row positions


# --------------------------------------
# Extracting columns
# --------------------------------------

# Select all columns under "Kathmandu"
print("\nColumns under 'Kathmandu':\n", branch_df2['Kathmandu'])

# Select only the "Students" column under "Kathmandu"
print("\nKathmandu → Students column:\n", branch_df2['Kathmandu']['Students'])


# --------------------------------------
# Extracting rows AND columns together
# --------------------------------------

# Extract specific rows & columns using iloc
# Rows: 0 and 4 → ('cse', 2019), ('ece', 2020)
# Columns: 1 and 2 → Kathmandu → Students, Pokhara → Avg_Package
print("\nSelected rows & columns:\n", branch_df2.iloc[[0, 4], [1, 2]])
