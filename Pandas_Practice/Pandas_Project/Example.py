import pandas as pd

data=pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\E-Commerce Data.csv",encoding='ISO-8859-1')

print(data.head())

#  Understand the Dataset

#  Basic Info: Shape of the dataset — number of rows (transactions) and columns
print("Dataset Shape (rows, columns):", data.shape)

#  Missing Values: Check how many null values exist in each column
print("\nMissing Values per Column:")
print(data.isnull().sum())

#  Duplicate Records: Identify if any duplicate rows exist
duplicate_count = data.duplicated().sum()
print(f"\nNumber of Duplicate Records: {duplicate_count}")

#  Cancelled / Refunded Invoices:
# Invoices that start with 'C' represent cancellations
cancelled_invoices = data[data['InvoiceNo'].str.startswith('C', na=False)]

print("\nCancelled / Refunded Invoices Preview:")
print(cancelled_invoices.head())

# Count of cancelled transactions
print("\nTotal Cancelled / Refunded Transactions:", cancelled_invoices.shape[0])

# How many countries are represented?
no_of_countries=len(data['Country'].unique())
print("Number of countries represented: ",no_of_countries)

# How many unique customers and products exist?

unique_customers=len(data['CustomerID'].unique())
unique_products=len(data['StockCode'].unique())
print(f"Number of unique customers are: {unique_customers}")
print(f"Number of unique products are: {unique_products}")

# Data Cleaning

# Remove Duplicates

data.drop_duplicates(inplace=True)

print("Number of data left after removing duplicate data",data.shape[0])

# Handle missing CustomerID

data=data.dropna(subset=['CustomerID'])

# Remove negative quantity or cancelled invoices

data=data[data['Quantity']>0]
data=data[~data['InvoiceNo'].str.startswith('C', na=False)]

# Ensure date format
data['InvoiceDate']=pd.to_datetime(data['InvoiceDate'])

# Add TotalSales column
data['TotalSales']=data['Quantity']*data['UnitPrice']
print(data.head())

# ===============================
# Key Performance Indicators (KPIs)
# ===============================

#  Total Revenue
total_revenue = data['TotalSales'].sum()
print("Total Revenue of the Store:", total_revenue)

# Unique Orders
total_orders = data['InvoiceNo'].nunique()
print("Total Unique Orders:", total_orders)

#  Unique Customers
unique_customers = data['CustomerID'].nunique()
print("Total Unique Customers:", unique_customers)

#  Average Order Value (AOV)
order_totals = data.groupby('InvoiceNo')['TotalSales'].sum()  # total revenue per order
average_order_value = order_totals.mean()
print("Average Order Value (AOV):", average_order_value)

#  Total Items Sold
total_items_sold = data['Quantity'].sum()
print("Total Items Sold:", total_items_sold)

#  Return Rate
cancelled_orders_count = cancelled_invoices['InvoiceNo'].nunique()
return_rate = cancelled_orders_count / total_orders
print("Return Rate:", return_rate)

#  Top 10 Best-Selling Products by Quantity
top10_products_qty = (
    data.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Best-Selling Products by Quantity:\n", top10_products_qty)

#  Top 10 Revenue-Generating Products
top10_products_revenue = (
    data.groupby('Description')['TotalSales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Revenue-Generating Products:\n", top10_products_revenue)


# ===============================
# Time-Based Trends Analysis
# ===============================

# ---------- Monthly Revenue Analysis ----------

# List of months in calendar order
months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']

# Extract month names from invoice dates
data['Month'] = data['InvoiceDate'].dt.month_name()

# Convert to categorical type with ordered months
data['Month'] = pd.Categorical(data['Month'], categories=months_order, ordered=True)

# Group by month and calculate total revenue
revenue_months = data.groupby('Month')['TotalSales'].sum()
print("Monthly Revenue:\n", revenue_months)

# Identify months with highest and lowest sales
highest_sales_month = revenue_months[revenue_months == revenue_months.max()]
lowest_sales_month = revenue_months[revenue_months == revenue_months.min()]

print("\nMonth(s) with Highest Sales:\n", highest_sales_month)
print("\nMonth(s) with Lowest Sales:\n", lowest_sales_month)


# ---------- Weekly Revenue Analysis ----------

# List of days in week order
days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Extract day names from invoice dates
data['Day'] = data['InvoiceDate'].dt.day_name()

# Convert to categorical type with ordered days
data['Day'] = pd.Categorical(data['Day'], categories=days_order, ordered=True)

# Group by day and calculate total revenue
revenue_day = data.groupby('Day')['TotalSales'].sum()

# Identify the busiest day(s)
busiest_day = revenue_day[revenue_day == revenue_day.max()]
print("\nBusiest Day(s) by Revenue:\n", busiest_day)


print(data.sample(10))

## ===============================
# Product Performance Analysis
# ===============================

# Products that sell the most by quantity
product_sell_quantity = data.groupby('Description')['Quantity'].sum()
max_quantity = product_sell_quantity.max()
top_products_quantity = product_sell_quantity[product_sell_quantity == max_quantity]
print("Products selling the most by quantity:\n", top_products_quantity, "\n")

# Products that generate the most revenue
product_revenue_sell = data.groupby('Description')['TotalSales'].sum()
max_revenue = product_revenue_sell.max()
top_products_revenue = product_revenue_sell[product_revenue_sell == max_revenue]
print("Products generating the most revenue:\n", top_products_revenue, "\n")

# Products that contribute the least to revenue
min_revenue = product_revenue_sell.min()
lowest_products_revenue = product_revenue_sell[product_revenue_sell == min_revenue]
print("Products contributing the least to revenue:\n", lowest_products_revenue)
