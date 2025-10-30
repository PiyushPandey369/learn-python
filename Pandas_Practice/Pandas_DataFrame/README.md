
# 📘 Pandas DataFrame — Complete Guide with Practical Examples

This repository provides a **comprehensive learning resource** for mastering the **Pandas DataFrame** — one of the most powerful data structures in Python for data analysis and manipulation.

It covers everything from **creating DataFrames** to **advanced operations** like grouping, merging, multi-indexing, and working with string or datetime data.  
Whether you're a **beginner**, **intermediate learner**, or a **data professional**, this folder serves as a step-by-step reference to explore and strengthen your understanding of Pandas.

---

## 🗂 Folder Structure

```text
Pandas_DataFrame/
├── DataFrame_Basic
├── DataFrame_GroupBy
├── DataFrame_Join
├── DataFrame_Multi_Indexing
├── DataFrame_String_DateTime
└── README.md
```


Each subfolder contains focused Python scripts demonstrating **concepts and operations** with practical examples, and  notes.

---

## 📚 Topics Covered

### 🧩 1. DataFrame Basics
Learn how to create and explore Pandas DataFrames:
- Creating DataFrames using **lists**, **dictionaries**, and **CSV files** (`pd.read_csv`)
- Attributes and properties: `.shape`, `.dtypes`, `.index`, `.columns`, `.values`
- Viewing data: `.head()`, `.tail()`, `.info()`, `.describe()`
- Handling missing values: `.isnull()`, `.hasnans`, `.dropna()`, `.fillna()`, `.drop_duplicates()`
- Renaming columns or indexes using `.rename()`

---

### 🧮 2. Mathematical & Statistical Operations
Perform numerical computations directly on DataFrames:
- Aggregate methods: `.sum()`, `.min()`, `.max()`, `.mean()`, `.median()`, `.std()`, `.var()`
- Applying functions across data using `.apply()`
- Descriptive analytics with `.describe()` and `.value_counts()`

---

### 🎯 3. Selecting & Filtering Data
Master data selection and conditional filtering:
- Column and row selection using `.loc[]` and `.iloc[]`
- Fancy indexing, slicing, and conditional filtering
- Adding new columns, changing data types (`.astype()`), and counting unique values (`.unique()`, `.nunique()`)

---

### 🧠 4. Important DataFrame Methods
Understand essential manipulation and transformation methods:
- Sorting and ranking: `.sort_values()`, `.rank()`
- Index management: `.reset_index()`
- Counting and frequency: `.value_counts()`

---

### 🧑‍🤝‍🧑 5. Grouping & Aggregation
Learn to analyze and summarize data using:
- The `groupby()` object and its attributes/methods
- Applying aggregate functions (`sum`, `mean`, `count`, `min`, `max`, etc.)
- Combining multiple aggregations
- Iterating over grouped data for customized analysis

---

### 🔗 6. Merging, Joining & Concatenation
Combine multiple DataFrames using:
- `pd.merge()` for SQL-style joins (inner, outer, left, right)
- `.join()` for index-based joins
- `pd.concat()` for stacking DataFrames vertically or horizontally

---

### 🏗️ 7. Multi-Indexing & Hierarchical Data
Work with multi-level (hierarchical) indexes:
- Creating and manipulating multi-indexed DataFrames
- Stacking and unstacking operations
- Using pivot tables for flexible data reshaping

---

### 🕒 8. String & DateTime Operations
Handle text and time-based data efficiently:
- String manipulation with `.str` methods
- Extracting, replacing, splitting, and formatting strings
- Working with datetime objects: parsing, formatting, resampling, and time-based indexing

---

## 💡 Who Is This For?

| Level | Description |
|-------|--------------|
| 🧑‍🎓 **Beginners** | Learn how to use Pandas DataFrames effectively from scratch. |
| 🧠 **Intermediate Learners** | Strengthen your understanding of indexing, grouping, and real-world data cleaning. |
| 🧑‍💻 **Experts / Data Analysts** | Sharpen your Pandas fluency with efficient operations, transformations, and advanced indexing techniques. |

---

## 🧰 Requirements

- **Python 3.8+**
- **Pandas library** (install using `pip install pandas`)
- **Jupyter Notebook / VS Code / any IDE**

Optional (for additional analysis or visualization):
```bash
pip install numpy matplotlib

```
## 🚀 How to Use

1. Clone this repository:
```
git clone https://github.com/yourusername/Pandas_DataFrame.git
```

2. Navigate to the project directory:
```bash
cd Pandas_DataFrame
```

3. Explore each folder for example scripts:
```bash
cd DataFrame_Basic
python create_dataframe.py
```

4. Experiment, modify, and learn by running the code snippets.

## References

[📘 Pandas Official Documentation](https://pandas.pydata.org/docs/)

[📗 Pandas User Guide – DataFrame](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html)

[📘 Kaggle Pandas Course](https://www.kaggle.com/learn/pandas)

[🌐 CampusX ](https://learnwith.campusx.in/)

## 🧑‍🏫 Author

Piyush Pandey

💻 Passionate about Data Analysis, Python, and Open-Source Learning