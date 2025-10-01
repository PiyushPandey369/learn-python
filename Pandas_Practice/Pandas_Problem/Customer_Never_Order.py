import pandas as pd
import numpy as np

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_cust=np.setdiff1d(customers['id'],orders['customerId'])
    print(ordered_cust)
    cust=customers[customers['id'].isin(ordered_cust)]
    return cust[['name']].rename(columns={'name':'Customers'}).reset_index(drop=True)

print(customers)
print(orders)

print(find_customers(customers,orders))