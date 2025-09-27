import pandas as pd

# -----------------------------
# Load CSV files
# -----------------------------
ipl = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\ipl-matches.csv')
movie = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv')

# -----------------------------
# Basic DataFrame info
# -----------------------------
# Number of rows and columns
# print("IPL DataFrame shape:", ipl.shape)       # (950, 20)
# print("Movie DataFrame shape:", movie.shape)   # (1629, 18)

# Column data types
# print("IPL DataFrame types:\n", ipl.dtypes)
# print("Movie DataFrame types:\n", movie.dtypes)

# Index information
# print("IPL DataFrame index:", ipl.index)
# print("Movie DataFrame index:", movie.index)

# Column names
# print("IPL columns:\n", ipl.columns)
# print("Movie columns:\n", movie.columns)

# Values as 2D array (NumPy array)
# print("IPL values:\n", ipl.values)
# print("Movie values:\n", movie.values)

# -----------------------------
# Fancy indexing examples
# -----------------------------

# Select multiple columns by names
# print(movie[['original_title', 'genres', 'title_x']])

# Select rows using iloc (position-based)
# print(ipl.iloc[0:5])          # first 5 rows
# print(movie.iloc[0:3, 0:3])   # first 3 rows, first 3 columns

# Select rows using loc (label-based)
# print(ipl.loc[0:4, ['match_id', 'team1', 'team2']])  # first 5 rows by label
