import pandas as pd
import numpy as np
# matches=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\matches.csv'
# courses=r'"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\courses.csv"'
# nov=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv'
# dec=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv'
# students=r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv'

# regs=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv')

courses=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\courses.csv')
students=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\students.csv')
nov=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month1.csv')
dec=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\reg-month2.csv')

# Combine November + December registrations into one DataFrame
regs = pd.concat([nov, dec], ignore_index=True)
print("-" * 10, "All Registrations (Nov + Dec)", "-" * 10)
print(regs)

print("-" * 10, "Courses", "-" * 10)
print(courses)

# 1) Find the total revenue of company
revenue = courses.merge(regs, how='inner', on='course_id')['price'].sum()
print("-" * 10, "1) Total Revenue", "-" * 10)
print(revenue)

# 2) Find the month by month revenue
temp_df = pd.concat([nov, dec], keys=['Nov', 'Dec']).reset_index()
month_revenue = (
    temp_df.merge(courses, how='inner', on='course_id')
           .groupby('level_0')['price'].sum()
)
print("-" * 10, "2) Month-wise Revenue", "-" * 10)
print(month_revenue)

# 3) Print the registration table (student + course + price)
registration_table = (
    regs.merge(students, on='student_id')
        .merge(courses, on='course_id')
        [['name', 'course_name', 'price']]
)
print("-" * 10, "3) Registration Table", "-" * 10)
print(registration_table)

# 4) Find students who enrolled in both months
common_ids = np.intersect1d(nov['student_id'], dec['student_id'])
both_months = students[students['student_id'].isin(common_ids)]
print("-" * 10, "4) Students in Both Months", "-" * 10)
print(both_months)

# 5) Find courses that got no enrollment (FIXED)
# ❌ Your code was using student_id instead of course_id
course_id_list = np.setdiff1d(courses['course_id'], regs['course_id'])
no_enrollment = courses[courses['course_id'].isin(course_id_list)]
print("-" * 10, "5) Courses with NO Enrollment", "-" * 10)
print(no_enrollment)

# 6) Find students that got no enrollment
std_id_list = np.setdiff1d(students['student_id'], regs['student_id'])
no_enrollment_std = students[students['student_id'].isin(std_id_list)]
print("-" * 10, "6) Students with NO Enrollment", "-" * 10)
print(no_enrollment_std)

# 7) Find top 3 students with most enrollments
top_students_enroll = (
    students.merge(regs, on='student_id')
            .groupby(['student_id','name'])
            .size()
            .sort_values(ascending=False)
            .head(3)
)
print("-" * 10, "7) Top 3 Students (Most Enrollments)", "-" * 10)
print(top_students_enroll)

# 8) Find top 3 students who spent the most money
top_students_spent = (
    regs.merge(students, on='student_id')
        .merge(courses, on='course_id')
        .groupby(['student_id','name'])['price']
        .sum()
        .sort_values(ascending=False)
        .head(3)
)
print("-" * 10, "8) Top 3 Students (Highest Spending)", "-" * 10)
print(top_students_spent)

