import pandas as pd

# Create a DataFrame
student_dict = {
    'iq': [100, 120, 90],
    'marks': [89, 79, 67],
    'package': [12, 8, 4]
}

student2 = pd.DataFrame(student_dict)

# Display the DataFrame
print("Student DataFrame:\n", student2, "\n")

# -----------------------------
# Statistical summaries
# -----------------------------
print("Sum of each column:\n", student2.sum(), "\n")
print("Minimum of each column:\n", student2.min(), "\n")
print("Maximum of each column:\n", student2.max(), "\n")
print("Median of each column:\n", student2.median(), "\n")
print("Mean of each column:\n", student2.mean(), "\n")
print("Variance of each column:\n", student2.var(), "\n")
print("Standard deviation of each column:\n", student2.std(), "\n")
