import pandas as pd
import numpy as np

# =============================
# Load CSV files
# =============================
ipl = pd.read_csv(
    r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\ipl-matches.csv'
)
movie = pd.read_csv(
    r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv'
)

# Uncomment these lines to explore the datasets
# print(ipl['TossDecision'].value_counts())  # Count of 'TossDecision' values
# print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())  # Non-numeric matches POTM count
# print(movie.info())  # Info about movie dataset
# print(movie.sort_values(['title_x','year_of_release'], ascending=[True, True]))  # Sorted movie data

# =============================
# Create sample DataFrame
# =============================
data_dict = [
    {"id": 1, "name": "Piyush", "age": 22, "city": "Delhi", "score": 85},
    {"id": 2, "name": "Rahul",  "age": np.nan, "city": "Mumbai", "score": 77},
    {"id": 3, "name": "Anita",  "age": 25, "city": np.nan, "score": 91},
    {"id": 4, "name": np.nan,   "age": 28, "city": "Kolkata", "score": np.nan},
    {"id": 5, "name": "Amit",   "age": 30, "city": "Chennai", "score": 66},
    {"id": 6, "name": "Rita",   "age": np.nan, "city": "Delhi", "score": 73},
    {"id": 7, "name": "Karan",  "age": 27, "city": np.nan, "score": 88},
    {"id": 8, "name": np.nan,   "age": 24, "city": "Pune", "score": 92},
    {"id": np.nan, "name": np.nan, "age": np.nan, "city": np.nan, "score": np.nan},
    {"id": 10, "name": "Alok",  "age": np.nan, "city": "Delhi", "score": 79},
]

data = pd.DataFrame(data_dict)

# =============================
# Inspect DataFrame
# =============================
# print(data)               # Print full data
# print(data.nunique())     # Count unique values per column
# print(data.isnull())      # Show True for NaN cells
# print(data.notnull())     # Show True for non-NaN cells

# =============================
# Drop or Fill Missing Values
# =============================
# print(data.dropna(subset=['name','age']))  # Drop rows where name or age is missing
# print(data.dropna(how="any"))              # Drop rows with any missing value
# print(data.dropna(how="all"))              # Drop rows where all values are missing
# print(data[['name','age']].fillna({'name': 'unknown', 'age': 0}))  # Fill missing values

# =============================
# Add 'gender' column
# =============================
data['gender'] = ["Male", "Male", "Female", np.nan, "Male", "Female", "Male", np.nan, np.nan, "Male"]
print("Data with gender column:\n", data)

# =============================
# Define function to map gender to Salutation
# =============================
def check_gender(gender):
    """
    Convert gender string to salutation:
    - 'Male' -> 'Mr'
    - 'Female' -> 'Mrs'
    - NaN or others -> np.nan
    """
    if pd.isna(gender):
        return np.nan
    gender_lower = gender.lower()
    if gender_lower == 'male':
        return "Mr"
    elif gender_lower == 'female':
        return "Mrs"
    else:
        return np.nan

# Apply function to 'gender' column
data['Salutation'] = data['gender'].apply(check_gender)

# =============================
# Calculate Rank based on 'score'
# =============================
# rank() assigns ranks to scores in descending order (highest score = 1)
data['Rank'] = data['score'].rank(ascending=False)

# =============================
# Final Data
# =============================
print("Final Data with Salutation and Rank:\n", data)
