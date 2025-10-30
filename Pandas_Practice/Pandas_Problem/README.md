# 🐼 Pandas Problem Solutions — LeetCode Style

This repository contains **Python solutions using the Pandas library** for various **LeetCode-style SQL problems**.  
Each script demonstrates how to solve common **data manipulation and analysis challenges** using **Pandas DataFrames**, mimicking SQL queries with clean and efficient Pythonic syntax.

---

## 📂 Folder Structure

```bash
Pandas_Problem/
├── Customer_Never_Order.py
├── Delete_Duplicate_Email.py
├── Department_Highest_Salary.py
├── Department_Top_Three_Salaries.py
├── Duplicate_Email.py
├── Employee_Earning.py
├── Game_Analysis.py
├── nth_highest_salary.py
├── Rank_Score.py
├── Rising_Temp.py
├── Second_Highest_Salary.py
└── README.md
```

---

## 📘 Problem Descriptions & Insights

| File Name | Description |
|------------|-------------|
| **Customer_Never_Order.py** | Identifies customers who have **never placed an order** — demonstrates left join and filtering of missing values using `merge()` and `isna()`. |
| **Delete_Duplicate_Email.py** | Removes **duplicate email entries**, showcasing the use of `drop_duplicates()` and efficient dataframe cleanup methods. |
| **Department_Highest_Salary.py** | Finds the **employee(s) with the highest salary** in each department using `groupby()` and filtering by maximum values. |
| **Department_Top_Three_Salaries.py** | Retrieves the **top three salaries per department**, illustrating ranking techniques with `rank()` or `nlargest()`. |
| **Duplicate_Email.py** | Detects **emails that appear more than once**, applying `groupby()` and `filter()` operations for frequency analysis. |
| **Employee_Earning.py** | Calculates **employees’ total earnings**, combining multiple tables using joins and aggregation with `groupby()` and `sum()`. |
| **Game_Analysis.py** | Performs **player and game statistics analysis**, often involving first login or session data, demonstrating `groupby()`, `min()`, and conditional filtering. |
| **nth_highest_salary.py** | Extracts the **N-th highest salary** using sorting, ranking, and unique value selection with Pandas methods like `rank()` and `drop_duplicates()`. |
| **Rank_Score.py** | Computes **ranking of students or scores**, highlighting techniques for ranking with ties using `rank(method='dense')`. |
| **Rising_Temp.py** | Finds **days when the temperature rose** compared to the previous day — demonstrates `shift()` and conditional filtering. |
| **Second_Highest_Salary.py** | Retrieves the **second highest salary**, a classic SQL-style query translated into Pandas logic with sorting and slicing. |

---

## 🧠 What You’ll Learn

✅ SQL-to-Pandas conversions (e.g., `SELECT`, `JOIN`, `GROUP BY`, `HAVING`)  
✅ Data cleaning, filtering, and aggregation techniques  
✅ Ranking and window functions with Pandas  
✅ Real-world data manipulation and problem-solving patterns  
✅ Writing efficient, readable, and reusable Pandas code

---

## 🛠️ Requirements

Before running the scripts, make sure you have:

```bash
pip install pandas
```

## 📚 References

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)

- [LeetCode Pandas Problems](https://leetcode.com/problemset/database/?topicSlugs=pandas)

## 💡 Author

Piyush Pandey
