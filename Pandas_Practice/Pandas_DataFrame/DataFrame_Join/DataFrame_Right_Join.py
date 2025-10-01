import pandas as pd

# matches=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv'
# courses=r'"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\courses.csv"'
# nov=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv'
# dec=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv'
# students=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv'


students=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv')
regs=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv')

# RIGHT JOIN
# Keeps all rows from 'regs' (right table) and adds matching rows from 'students'.
# If no match is found, NaN will be placed.

right_join=students.merge(regs,how='right',on='student_id')
print("-" * 10, "RIGHT JOIN (All Registrations, matching student details if available)", "-" * 10)
print(right_join)