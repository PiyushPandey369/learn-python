import pandas as pd

data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged=employee.merge(department,left_on='departmentId',right_on='id')
    print(merged)
    merged['rank']=merged.groupby('name_y')['salary'].rank(method='dense',ascending=False)
    print(merged)
    merged.sort_values(by='rank',inplace=True)
    print(merged)
    merged=merged[merged['rank']<=3]
    merged.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}, inplace=True)
    print(merged[['Department','Employee','Salary']].sort_values(by='Department'))



print(employee)
print(department)
top_three_salaries(employee,department)