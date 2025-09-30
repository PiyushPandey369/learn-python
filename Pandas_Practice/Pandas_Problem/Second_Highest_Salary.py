import pandas as pd
import numpy as np
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
def second_highest_salary(employee):
    unique_emp=employee['salary'].drop_duplicates()
    unique_emp=unique_emp.sort_values(ascending=False).reset_index(drop=True)
    if len(unique_emp)>1:
        a=unique_emp.iloc[1]
        return pd.DataFrame({"Second_Highest":[a]})
    else:
        return pd.DataFrame({"Second_Highest":[None]})

print(second_highest_salary(employee)) 
