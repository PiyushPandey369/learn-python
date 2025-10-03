import pandas as pd
import numpy as np

# -------------------------
# MultiIndex from tuples
# -------------------------
index_val = [
    ('cse', 2019), ('cse', 2020), ('cse', 2021), ('cse', 2022),
    ('ece', 2019), ('ece', 2020), ('ece', 2021), ('ece', 2022)
]

# Create MultiIndex (branch, year)
multiindex = pd.MultiIndex.from_tuples(index_val)
# Print the "year" level (2nd level) from the MultiIndex
print(multiindex.levels[1])

# Create a Series with MultiIndex
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=multiindex)
print(s)


# -------------------------
# MultiIndex from product (Cartesian product)
# -------------------------
index_val1 = pd.MultiIndex.from_product(
    [['cse', 'ece'], [2019, 2020, 2021, 2022]]
)

# MultiIndex DataFrame (rows indexed by branch, year)
branch_df1 = pd.DataFrame(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [6, 7],
        [7, 8],
        [9, 10],
        [15, 60],
        [61, 71]
    ],
    index=index_val1,
    columns=['avg_package', 'students']
)
print(branch_df1)


# -------------------------
# MultiIndex on both rows & columns
# -------------------------
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

# Display the DataFrame
print(branch_df2)


# -------------------------
# Stacking and Unstacking
# -------------------------
# Unstack moves one level of the row index into the columns
print(branch_df2.unstack())
