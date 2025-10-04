import pandas as pd  
import numpy as np   

# Load the Titanic dataset 

titanic = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\titanic.csv")

# ------------------------------
# STRING OPERATIONS ON DATAFRAME
# ------------------------------

# Pandas provides 'str' accessor to perform vectorized string operations
# on Series (columns of text data) efficiently.
# Common string functions:
# - lower(): convert to lowercase
# - upper(): convert to uppercase
# - capitalize(): first character uppercase, rest lowercase
# - title(): first character of each word uppercase
# - len(): length of string
# - strip(): remove leading/trailing spaces

# Examples:
# print(titanic['Name'].str.lower())      # All names in lowercase
# print(titanic['Name'].str.upper())      # All names in uppercase
# print(titanic['Name'].str.capitalize()) # Capitalize first letter
# print(titanic['Name'].str.title())      # Title case for each word
# print(titanic[(titanic['Name'].str.len()) == (titanic['Name'].str.len().max())])  # Longest name

# ------------------------------
# SPLITTING AND EXTRACTING NAMES
# ------------------------------

# Extract the last name from the 'Name' column
# Names in Titanic dataset are usually in format: "LastName, Salutation FirstName"
titanic['LastName'] = titanic['Name'].str.split(",").str.get(0)

# Extract the salutation (Mr, Mrs, Miss, etc.) from the 'Name' column
# Split by space and get the second element (index 1)
titanic['Salutation'] = titanic['Name'].str.split(" ").str.get(1)

# Extract the first name from the 'Name' column
# Steps:
# 1. Split by comma, take second part (Salutation + FirstName)
# 2. Strip extra spaces
# 3. Split by space, take the second element which is the actual first name
titanic['FirstName'] = titanic['Name'].str.split(",").str.get(1).str.strip().str.split(' ', n=1).str.get(1)

# Print first few rows to verify changes
print(titanic.head())

# Replace 'Ms' with 'Miss' in the 'Salutation' column
print(titanic['Salutation'].str.replace('Ms', 'Miss'))

# Verify changes after replacement
print(titanic.head())

# ------------------------------
# FILTERING BASED ON STRING CONDITIONS
# ------------------------------

# Filter rows where FirstName starts with 'A'
print(titanic[titanic['FirstName'].str.startswith('A')])

# Filter rows where FirstName contains 'john' (case-insensitive)
print(titanic[titanic['FirstName'].str.contains('john', case=False)])

# Filter rows where LastName starts and ends with a vowel (Regular-Expression)
print(titanic[titanic['LastName'].str.contains('^[aeiouAEIOU].+[aeiouAEIOU]$')])

# Access every second character in the 'Name' column
print(titanic['Name'].str[::2])
