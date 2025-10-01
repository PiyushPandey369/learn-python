import pandas as pd

# matches=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv'
# courses=r'"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\courses.csv"'
# nov=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv'
# dec=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv'
# students=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv'


students=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv')
regs=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv')

# OUTER JOIN (Full Join)
# Keeps all rows from both DataFrames.
# - If a student exists but no registration -> NaN in registration columns.
# - If a registration exists but no student details -> NaN in student columns.
outer_join = students.merge(regs, how='outer', on='student_id')
print("-" * 10, "OUTER JOIN (All Students + All Registrations, combine everything)", "-" * 10)
print(outer_join)

