import pandas as pd

# Load CSV files
ipl = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\ipl-matches.csv')
movie = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv')

# Create student DataFrames
student_dict = {
    'name': ["Hemant", "Rakesh", "Modi"],
    'iq': [100, 120, 90],
    'marks': [89, 79, 67],
    'package': [12, 8, 4]
}

student1 = pd.DataFrame(student_dict)
student2 = pd.DataFrame(student_dict)

# -----------------------------
# Selecting columns
# -----------------------------

# Single column
print(movie['title_x'])

# Multiple columns using fancy indexing
print(movie[['original_title', 'genres', 'title_x']])

# -----------------------------
# Selecting rows
# -----------------------------

# Using loc (label-based indexing)
print(student1.loc[0])  # first row by label

# Using iloc (position-based indexing)
print(movie.iloc[0:5])         # first 5 rows
print(movie.iloc[0:3, 0:3])    # first 3 rows, first 3 columns

# -----------------------------
# Fancy indexing using column names
# -----------------------------
# Selecting the first column (like movie[[0]] but correctly)
first_column_name = movie.columns[0]  # get the name of the first column
print(movie[[first_column_name]])     # fancy indexing
