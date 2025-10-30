
# 🛍️ E-Commerce Sales Data Analysis

## 📖 Project Description

This project performs an **end-to-end data analysis** of an e-commerce dataset using **Python and Pandas**. The goal is to clean, explore, and analyze online retail transactional data to derive **business insights** such as sales performance, customer behavior, and product trends.  
It showcases practical **data analysis and reporting skills**, from **data preprocessing** to **KPI calculation** and **customer segmentation**.

---

## 📊 Dataset

**Source:** [E-Commerce Data — Kaggle](https://www.kaggle.com/datasets)  
**Description:** The dataset contains transactional data from an online retail store. Each record represents an item purchased in an order, including details such as:

| Column | Description |
|--------|--------------|
| `InvoiceNo` | Unique identifier for each transaction |
| `StockCode` | Product code |
| `Description` | Product description |
| `Quantity` | Quantity of each product per transaction |
| `InvoiceDate` | Date and time of purchase |
| `UnitPrice` | Price per item |
| `CustomerID` | Unique identifier for each customer |
| `Country` | Country of customer |

---

## 🎯 Objectives

The primary objectives of this analysis are:

- To **clean** and **prepare** the dataset for reliable analysis  
- To compute **key performance indicators (KPIs)** such as total revenue, average order value, and total customers  
- To uncover **sales trends over time** (monthly and weekly)  
- To identify **top-performing products** and **high-value customers**  
- To perform **customer segmentation** based on recency and purchase frequency  

This project provides valuable insights for:

- **E-commerce Business Managers & Stakeholders** — to monitor and improve performance  
- **Marketing Teams** — to plan campaigns based on product and customer behavior  
- **Aspiring Data Analysts/Scientists** — as a strong **portfolio project** demonstrating real-world data analysis skills  

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Pandas**
- **NumPy**
- **Matplotlib / Seaborn** (for visualization)
- **Jupyter Notebook**

---

## ⚙️ Installation & Usage

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/E-Commerce-Data-Analysis.git
```
2. **Navigate to the project directory:**
```bash
cd E-Commerce-Data-Analysis
```

3. **Install required dependencies:**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

4. **Run the analysis notebook:**
```bash
jupyter notebook E_Commerce.ipynb
```
## 🧩 Methodology & Code Walkthrough
### 1. Data Understanding & Initial Inspection

``data.shape`` → Checked dataset dimensions

``data.isnull().sum()`` → Identified missing values

``data.duplicated().sum()`` → Counted duplicate records

These steps established an overview of data quality and completeness.

### 2. Data Cleaning

- Removed duplicates:
```bash
data.drop_duplicates(inplace=True)
```

- Handled missing values in CustomerID:
```bash
data.dropna(subset=['CustomerID'], inplace=True)
```

- Removed cancelled and negative transactions:
```bash
data = data[(data['Quantity'] > 0) & ~data['InvoiceNo'].str.startswith('C', na=False)]
```

- Converted InvoiceDate to datetime for time-series analysis:
```bash
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
```

- Created a new TotalSales column:
```bash
data['TotalSales'] = data['Quantity'] * data['UnitPrice']
```

These transformations ensured clean and consistent data for analysis.

## 3. 📊 Key Performance Indicator (KPI) Calculation

| KPI | Formula / Code | Description |
|-----|----------------|-------------|
| **Total Revenue** | `data['TotalSales'].sum()` | Total earnings from all sales |
| **Unique Orders** | `data['InvoiceNo'].nunique()` | Number of unique transactions |
| **Unique Customers** | `data['CustomerID'].nunique()` | Active customer count |
| **Average Order Value (AOV)** | `data.groupby('InvoiceNo')['TotalSales'].sum().mean()` | Average spending per order |
| **Total Items Sold** | `data['Quantity'].sum()` | Units sold across all transactions |
| **Return Rate** | Analyzed cancelled invoices | Percentage of orders returned |

## 📈 4. Time-Based Trend Analysis

### Monthly Analysis
- **Extracted month and weekday:**
```
data['Month'] = data['InvoiceDate'].dt.month_name()
data['Day'] = data['InvoiceDate'].dt.day_name()
```

- **Ordered months for better visualization:**
```
data['Month'] = pd.Categorical(data['Month'], categories=[...], ordered=True)
```

- **Monthly Revenue:**
```
data.groupby('Month')['TotalSales'].sum()
```
- **Day-wise Revenue:**
```
data.groupby('Day')['TotalSales'].sum()
```
## 5. Customer Analysis & Segmentation

- **Top Countries by Revenue:**
```
data.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)
```

- **Average Purchase Frequency:**
```
data.groupby('CustomerID')['InvoiceNo'].nunique().mean()
```

- **Top 10 Customers by Spending:**
```
data.groupby('CustomerID')['TotalSales'].sum().sort_values(ascending=False).head(10)
```

- **Recency Calculation:**
```python
recency = snapshot_date - data.groupby('CustomerID')['InvoiceDate'].max()
```
## 🧭 Conclusion

This project successfully demonstrates how Python and Pandas can be used to derive actionable business insights from raw e-commerce data. Through systematic data cleaning, KPI computation, and behavioral segmentation, it provides a comprehensive understanding of:

- Sales performance

- Customer patterns

- Product demand trends

### 🚀 Next Steps

- Implement RFM (Recency, Frequency, Monetary) analysis for deeper segmentation

- Create interactive dashboards using Power BI or Plotly Dash

- Apply predictive modeling for customer retention and sales forecasting

## 🤝 Acknowledgments

Dataset courtesy of [Kaggle](https://www.kaggle.com/)


Developed by Piyush Pandey — Aspiring Data Analyst & Python Enthusiast.