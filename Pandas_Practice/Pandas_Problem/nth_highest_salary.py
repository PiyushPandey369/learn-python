import pandas as pd

data = [[1, 100],[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})
# print(employee)

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_emp=employee['Salary'].drop_duplicates()
    if N<=0:
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    if len(unique_emp)>=abs(N):
        nth_highest_sal=unique_emp.nlargest(N).iloc[-1]
        return pd.DataFrame({f"getNthHighestSalary({N})":[nth_highest_sal]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    

n=int(input("Enter the nth values"))
print(nth_highest_salary(employee,n))





