import pandas as pd
import numpy as np

# -----------------------------
# Load dataset
# -----------------------------
movies = pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\imdb-top-1000.csv')

# -----------------------------
# Group by Genre
# -----------------------------
genres = movies.groupby('Genre')

# -----------------------------
# Number of groups
# -----------------------------
print("Total number of genres (groups):", len(genres))
print("Unique genres (alternative):", movies['Genre'].nunique(), "\n")

# -----------------------------
# Size of each group
# -----------------------------
print("Movies count per genre:")
print(genres.size(), "\n")
# Alternative
print("Movies count per genre (using value_counts):")
print(movies['Genre'].value_counts(), "\n")

# -----------------------------
# First, last, nth values in each group
# -----------------------------
print("First movie in each genre:")
print(genres.first(), "\n")

print("Last movie in each genre:")
print(genres.last(), "\n")

print("7th movie in each genre (if exists):")
print(genres.nth(6), "\n")

# -----------------------------
# Data for a particular group
# -----------------------------
print("All movies in Fantasy genre:")
print(genres.get_group('Fantasy'), "\n")
# Alternative
print(movies[movies['Genre'] == 'Fantasy'], "\n")

# -----------------------------
# Groups dictionary (Genre -> row indices)
# -----------------------------
print("Groups mapping (genre -> indices):")
print(genres.groups, "\n")

# -----------------------------
# Descriptive statistics per group
# -----------------------------
print("Descriptive statistics for each genre:")
print(genres.describe(), "\n")

# -----------------------------
# Random samples
# -----------------------------
print("Random 1 sample from groups:")
print(genres.sample(), "\n")

print("Random 2 samples with replacement:")
print(genres.sample(2, replace=True), "\n")

# -----------------------------
# Count of unique values in each group
# -----------------------------
print("Number of unique values in each group:")
print(genres.nunique(), "\n")
