import pandas as pd

students=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv')

print(students)

# SELF JOIN
# We want to join students with themselves:
# - 'partner' column (from left side) should match 'student_id' (from right side).
self_join = students.merge(
    students,
    how='inner',
    left_on='partner',    # partner column refers to another student's ID
    right_on='student_id' # match with student_id column
)

print("-" * 10, "Self Join (Students with their partners)", "-" * 10)
print(self_join)

# Display only the relevant names (student and their partner)
print("-" * 10, "Students and their Partners", "-" * 10)
print(self_join[['name_x', 'name_y']])