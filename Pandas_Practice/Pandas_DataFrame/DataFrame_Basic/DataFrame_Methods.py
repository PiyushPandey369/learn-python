import pandas as pd

# -----------------------------
# Load CSV files
# -----------------------------
ipl = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\ipl-matches.csv')
movie = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv')

# -----------------------------
# Quick look at the data
# -----------------------------
# print(ipl.head())    # first 5 rows of IPL data
# print(movie.tail())  # last 5 rows of movie data
# print(movie.sample()) # random row from movie data

# -----------------------------
# DataFrame info & summary
# -----------------------------
# print(ipl.info())    # summary of IPL DataFrame
# print(movie.info())  # summary of Movie DataFrame
# print(ipl.describe()) # statistical summary (numerical columns)
# print(movie.describe())

# -----------------------------
# Student data as a list of lists
# -----------------------------
student_data = [
    [100, 80, 10],
    [120, 90, 15],
    [90, 70, 5],
    [80, 65, 3],
    [0, 0, 0],
    [0, 0, 0]
]

student_df = pd.DataFrame(student_data, columns=['IQ', 'Marks', 'Package'])
# print(student_df)

# -----------------------------
# Checking for missing or duplicated data
# -----------------------------
# print(ipl.isnull().sum())          # count of missing values in each column
# print(student_df.duplicated().sum()) # count of duplicated rows

# -----------------------------
# Renaming columns
# -----------------------------
# Example without changing original DataFrame
# print(student_df.rename(columns={'Marks': 'Percentage', 'Package': 'Cash'}))

# Example with inplace change
# student_df.rename(columns={'Marks': 'Percentage', 'Package': 'Cash'}, inplace=True)
# print(student_df) 