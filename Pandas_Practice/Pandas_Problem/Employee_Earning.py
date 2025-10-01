import pandas as pd
import numpy as np

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})

print(employee)


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    emp=employee.merge(employee,how='inner',left_on='managerId',right_on='id')[['name_x','salary_x','salary_y']]
    print(emp)
    emp=emp[(emp['salary_x'])>(emp['salary_y'])]
    print(emp)
    return emp[['name_x']].rename(columns={'name_x': 'Employee'})

print(find_employees(employee))