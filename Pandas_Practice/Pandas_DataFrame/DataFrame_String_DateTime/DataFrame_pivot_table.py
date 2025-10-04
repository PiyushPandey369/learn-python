import pandas as pd
import numpy as np

expense_df=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\expense_data.csv")
titanic=(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\titanic.csv")

# Comparing groupby() and pivot_table() in pandas

# Both of these calculate the mean 'INR' value for each 'Category'
print(expense_df.groupby('Category')['INR'].mean())
print(expense_df.pivot_table(index='Category', values='INR', aggfunc='mean'))
'''

#  Notes on pivot_table():
# --------------------------------------------------------------------
# pivot_table() is used to summarize and analyze data similar to Excel's Pivot Table.
#
#  Common Parameters:
#   - index: The column(s) to group by (similar to rows in Excel Pivot)
#   - values: The column(s) on which to apply the aggregation function
#   - columns: Optional — creates sub-columns for comparison (e.g., by Month)
#   - aggfunc: Aggregation function(s) to apply.
#              By default it's 'mean', but you can use:
#              ['mean', 'median', 'sum', 'std', 'var', 'count', 'max', 'min']
#   - margins: Adds a total row/column (like "All" or "Total")
#   - margins_name: Custom label for the total (default is 'All')
#
# 
#   - If you omit 'values', pandas automatically applies the aggfunc
#     to all numeric columns.
#
# Example:
# expense_df.pivot_table(index='Category',
#                        columns='Month',
#                        values='INR',
#                        aggfunc='sum',
#                        margins=True,
#                        margins_name='Overall')
#

'''



