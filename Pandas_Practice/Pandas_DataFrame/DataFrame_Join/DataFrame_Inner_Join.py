import pandas as pd

# matches=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv'
# courses=r'"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\courses.csv"'
# nov=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv'
# dec=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv'
# students=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv'


students=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv')
regs=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv')

print("-"*10,"Students Details","-"*10)
print(students)

print("-"*10,"Register Details","-"*10)
print(regs)


# Inner Join returns only matching rows from both DataFrames
print("-" * 10, "Inner Join (Common Students Only)", "-" * 10)
inner_join = students.merge(regs, how='inner', on='student_id')
print(inner_join)
