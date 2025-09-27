import pandas as pd

# -------------------------------
# Load Virat Kohli's IPL data
# -------------------------------
vk = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\kohli_ipl.csv",
    index_col="match_no"
).squeeze("columns")   # Convert to Series if possible

# -------------------------------
# Load Bollywood movies dataset
# -------------------------------
movies = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\bollywood.csv",
    index_col="movie"
).squeeze("columns")

# -------------------------------
# Exploring Virat Kohli IPL Data
# -------------------------------

# First 5 matches
# print("Virat Kohli's first 5 IPL matches:")
# print(vk.head())

# Last 5 matches
# print("\nVirat Kohli's last 5 IPL matches:")
# print(vk.tail())

# Random match record
# print("\nRandom match sample:")
# print(vk.sample())

# Frequency of values in vk
# print("\nFrequency of values in IPL data:")
# print(vk.value_counts())

# -------------------------------
# Exploring Bollywood Movies Data
# -------------------------------

# Frequency of movie values
print("\nBollywood movies frequency count:")
print(movies.value_counts())

# Sort by movie names (index)
# print("\nMovies sorted by index:")
# print(movies.sort_index())

# Sort by values (descending)
# print("\nMovies sorted by values (descending):")
# print(movies.sort_values(ascending=False))
