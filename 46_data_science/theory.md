# Data Science Essentials - Theory

## Table of Contents
1. [NumPy Fundamentals](#numpy-fundamentals)
2. [Pandas Essentials](#pandas-essentials)
3. [Matplotlib Basics](#matplotlib-basics)
4. [SciPy Overview](#scipy-overview)
5. [Data Analysis Workflows](#data-analysis-workflows)

---

## NumPy Fundamentals

NumPy (Numerical Python) is the foundation of scientific computing in Python. It provides efficient array operations and mathematical functions.

### Why NumPy?

```
Python List vs NumPy Array Performance:

Python List (1M elements):     ~100ms
NumPy Array (1M elements):     ~1ms
                                ↓
                        100x faster!
```

### NumPy Arrays

Arrays are homogeneous, fixed-size, multi-dimensional containers.

```python
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])           # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])    # 2D array
arr3 = np.zeros((3, 3))                     # 3x3 zeros
arr4 = np.ones((2, 4))                      # 2x4 ones
arr5 = np.arange(0, 10, 2)                  # [0, 2, 4, 6, 8]
arr6 = np.linspace(0, 1, 5)                 # [0, 0.25, 0.5, 0.75, 1]
```

### Array Properties

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape       # (2, 3) - dimensions
arr.ndim        # 2 - number of dimensions
arr.size        # 6 - total elements
arr.dtype       # dtype('int64') - data type
arr.itemsize    # 8 - bytes per element
```

### Array Indexing and Slicing

```
Visual representation of 2D array indexing:

    Col 0   Col 1   Col 2
Row 0  [1,     2,     3]     arr[0, 1] = 2
Row 1  [4,     5,     6]     arr[1, :] = [4, 5, 6]
Row 2  [7,     8,     9]     arr[:, 2] = [3, 6, 9]
```

```python
# 1D indexing
arr = np.array([1, 2, 3, 4, 5])
arr[0]          # 1
arr[-1]         # 5
arr[1:4]        # [2, 3, 4]
arr[::2]        # [1, 3, 5]

# 2D indexing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr[0, 0]       # 1
arr[1, :]       # [4, 5, 6] - row 1
arr[:, 1]       # [2, 5, 8] - column 1
arr[0:2, 1:3]   # [[2, 3], [5, 6]] - subarray
```

### Boolean Indexing

```python
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3              # [False, False, False, True, True]
result = arr[mask]          # [4, 5]

# Shorthand
result = arr[arr > 3]       # [4, 5]
```

### Array Operations

```python
# Element-wise operations (vectorized)
arr = np.array([1, 2, 3, 4])
arr + 10        # [11, 12, 13, 14]
arr * 2         # [2, 4, 6, 8]
arr ** 2        # [1, 4, 9, 16]

# Array-array operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr1 + arr2     # [5, 7, 9]
arr1 * arr2     # [4, 10, 18]

# Broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr + np.array([10, 20, 30])  # Adds to each row
# [[11, 22, 33], [14, 25, 36]]
```

### Broadcasting Rules

```
Broadcasting allows operations on arrays of different shapes:

Shape (3, 1)  +  Shape (3,)   →  Shape (3, 3)
  [[1],           [10, 20, 30]     [[11, 21, 31],
   [2],                             [12, 22, 32],
   [3]]                             [13, 23, 33]]
```

### Universal Functions (ufuncs)

```python
arr = np.array([1, 4, 9, 16])

# Math functions
np.sqrt(arr)        # [1, 2, 3, 4]
np.exp(arr)         # e^x for each element
np.log(arr)         # natural log
np.sin(arr)         # sine

# Statistical functions
arr.sum()           # 30
arr.mean()          # 7.5
arr.std()           # standard deviation
arr.min()           # 1
arr.max()           # 16

# Axis operations
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr2d.sum(axis=0)   # [5, 7, 9] - column sums
arr2d.sum(axis=1)   # [6, 15] - row sums
```

### Array Reshaping

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 3)   # [[1, 2, 3], [4, 5, 6]]
arr.reshape(3, 2)   # [[1, 2], [3, 4], [5, 6]]
arr.reshape(-1, 1)  # [[1], [2], [3], [4], [5], [6]]

# Transpose
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr2d.T             # [[1, 4], [2, 5], [3, 6]]

# Flatten
arr2d.flatten()     # [1, 2, 3, 4, 5, 6]
arr2d.ravel()       # [1, 2, 3, 4, 5, 6] (view, not copy)
```

---

## Pandas Essentials

Pandas provides high-level data structures and tools for data analysis.

### Series

A Series is a 1D labeled array.

```python
import pandas as pd

# Creating Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s3 = pd.Series({'a': 1, 'b': 2, 'c': 3})

# Accessing elements
s2['a']         # 1
s2[0]           # 1
s2['a':'c']     # a:1, b:2, c:3
```

### DataFrame

A DataFrame is a 2D labeled data structure (like a table).

```
DataFrame Structure:

       Column1  Column2  Column3
Row1      10       20       30
Row2      40       50       60
Row3      70       80       90
   ↑                           ↑
 Index                      Values
```

```python
# Creating DataFrames
df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

df2 = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['A', 'B', 'C'],
    index=['row1', 'row2', 'row3']
)

# From NumPy array
df3 = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['A', 'B', 'C']
)
```

### DataFrame Operations

```python
# Viewing data
df.head()           # First 5 rows
df.tail(3)          # Last 3 rows
df.info()           # Summary information
df.describe()       # Statistical summary
df.shape            # (rows, columns)
df.columns          # Column names
df.index            # Row indices

# Selecting data
df['name']          # Single column (Series)
df[['name', 'age']] # Multiple columns (DataFrame)
df.loc[0]           # Row by label
df.iloc[0]          # Row by position
df.loc[0, 'name']   # Specific cell by label
df.iloc[0, 0]       # Specific cell by position

# Filtering
df[df['age'] > 25]              # Boolean indexing
df[df['salary'].between(50000, 65000)]
df[(df['age'] > 25) & (df['salary'] < 65000)]
```

### Adding and Removing Data

```python
# Adding columns
df['bonus'] = df['salary'] * 0.1
df['full_name'] = df['first_name'] + ' ' + df['last_name']

# Adding rows
new_row = pd.Series({'name': 'David', 'age': 28, 'salary': 55000})
df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

# Removing columns
df.drop('bonus', axis=1, inplace=True)
df.drop(['bonus', 'full_name'], axis=1, inplace=True)

# Removing rows
df.drop(0, axis=0, inplace=True)        # Drop row 0
df = df[df['age'] > 25]                 # Filter out rows
```

### Data Manipulation

```python
# Sorting
df.sort_values('age')                       # Ascending
df.sort_values('salary', ascending=False)   # Descending
df.sort_values(['age', 'salary'])           # Multiple columns

# Grouping
df.groupby('department')['salary'].mean()
df.groupby('department').agg({
    'salary': ['mean', 'sum', 'count'],
    'age': 'mean'
})

# Aggregation
df['salary'].sum()
df['salary'].mean()
df['salary'].max()
df.agg({'salary': 'mean', 'age': 'max'})

# Apply functions
df['salary_k'] = df['salary'].apply(lambda x: x / 1000)
df['age_group'] = df['age'].apply(lambda x: 'young' if x < 30 else 'senior')
```

### Handling Missing Data

```python
# Detecting missing data
df.isnull()             # Boolean DataFrame
df.isnull().sum()       # Count per column
df.notnull()            # Opposite of isnull()

# Dropping missing data
df.dropna()             # Drop rows with any NaN
df.dropna(axis=1)       # Drop columns with any NaN
df.dropna(thresh=2)     # Drop rows with < 2 non-NaN values

# Filling missing data
df.fillna(0)            # Fill with 0
df.fillna(df.mean())    # Fill with column mean
df.fillna(method='ffill')  # Forward fill
df.fillna(method='bfill')  # Backward fill
```

### Merging and Joining

```python
# Concatenation
pd.concat([df1, df2])               # Vertical (rows)
pd.concat([df1, df2], axis=1)       # Horizontal (columns)

# Merging (like SQL joins)
pd.merge(df1, df2, on='key')        # Inner join
pd.merge(df1, df2, on='key', how='left')
pd.merge(df1, df2, on='key', how='right')
pd.merge(df1, df2, on='key', how='outer')

# Join (merge on index)
df1.join(df2)
df1.join(df2, how='outer')
```

### Reading and Writing Data

```python
# CSV files
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Excel files
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df.to_excel('output.xlsx', index=False)

# JSON files
df = pd.read_json('data.json')
df.to_json('output.json')

# SQL databases
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table', conn)
df.to_sql('table_name', conn, if_exists='replace')
```

---

## Matplotlib Basics

Matplotlib is the foundational plotting library in Python.

### Basic Plotting

```python
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Line Plot')
plt.show()

# Multiple lines
plt.plot(x, y, label='y = x²')
plt.plot(x, [i*2 for i in x], label='y = 2x')
plt.legend()
plt.show()
```

### Plot Types

```python
# Scatter plot
plt.scatter(x, y)
plt.show()

# Bar plot
plt.bar(['A', 'B', 'C'], [10, 20, 15])
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()

# Pie chart
plt.pie([30, 25, 20, 25], labels=['A', 'B', 'C', 'D'])
plt.show()
```

### Customization

```python
# Styling
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o')
plt.plot(x, y, 'ro-')  # Shorthand: red circles with line

# Figure size
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.show()

# Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(x, y)
axes[1, 1].hist(y)
plt.tight_layout()
plt.show()
```

### Integration with Pandas

```python
# Direct plotting from DataFrame
df.plot()                   # Line plot of all columns
df.plot(kind='bar')         # Bar chart
df.plot(kind='scatter', x='age', y='salary')
df['salary'].plot(kind='hist')
df.plot(kind='box')         # Box plot

# Styling
df.plot(style=['o-', 'x--'], figsize=(10, 6))
```

---

## SciPy Overview

SciPy builds on NumPy and provides advanced scientific computing tools.

### Key Modules

```python
from scipy import stats      # Statistics
from scipy import optimize   # Optimization
from scipy import integrate  # Integration
from scipy import linalg     # Linear algebra
from scipy import signal     # Signal processing
from scipy import sparse     # Sparse matrices
```

### Statistical Functions

```python
from scipy import stats

# Distributions
data = np.random.randn(100)
mean, std = stats.norm.fit(data)

# Statistical tests
t_stat, p_value = stats.ttest_ind(group1, group2)
correlation, p_value = stats.pearsonr(x, y)

# Descriptive statistics
stats.describe(data)
```

### Optimization

```python
from scipy import optimize

# Finding minimum
def f(x):
    return x**2 + 10*np.sin(x)

result = optimize.minimize(f, x0=0)
print(result.x)  # Optimal x value

# Root finding
def equation(x):
    return x**3 - 2*x - 5

root = optimize.fsolve(equation, x0=2)
```

### Integration

```python
from scipy import integrate

# Definite integral
result, error = integrate.quad(lambda x: x**2, 0, 1)  # ∫₀¹ x² dx

# Numerical integration
x = np.linspace(0, 10, 100)
y = np.sin(x)
area = integrate.trapz(y, x)
```

---

## Data Analysis Workflows

### Complete Analysis Pipeline

```
Data Analysis Workflow:

1. Import Data
      ↓
2. Explore & Clean
      ↓
3. Transform & Feature Engineering
      ↓
4. Analyze
      ↓
5. Visualize
      ↓
6. Report Results
```

### Step 1: Import Data

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Initial inspection
print(df.head())
print(df.info())
print(df.describe())
```

### Step 2: Explore and Clean

```python
# Check for missing values
print(df.isnull().sum())

# Handle missing values
df = df.dropna()  # or
df = df.fillna(df.mean())

# Check for duplicates
df = df.drop_duplicates()

# Data types
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')
```

### Step 3: Transform

```python
# Create new features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Binning
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100],
                          labels=['child', 'young', 'middle', 'senior'])

# Normalize
from sklearn.preprocessing import StandardScaler
df['salary_normalized'] = StandardScaler().fit_transform(df[['salary']])
```

### Step 4: Analyze

```python
# Group analysis
summary = df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'profit': 'sum'
})

# Correlation
correlation_matrix = df.corr()

# Statistical tests
from scipy import stats
t_stat, p_value = stats.ttest_ind(df[df['group'] == 'A']['value'],
                                    df[df['group'] == 'B']['value'])
```

### Step 5: Visualize

```python
# Distribution
df['salary'].hist(bins=30)
plt.title('Salary Distribution')
plt.show()

# Trends
df.groupby('month')['sales'].sum().plot()
plt.title('Monthly Sales')
plt.show()

# Relationships
plt.scatter(df['age'], df['salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Categorical
df.groupby('department')['salary'].mean().plot(kind='bar')
plt.show()
```

### Step 6: Report

```python
# Export results
summary.to_csv('analysis_summary.csv')
df.to_excel('processed_data.xlsx', index=False)

# Create report
report = f"""
Data Analysis Report
====================

Total Records: {len(df)}
Date Range: {df['date'].min()} to {df['date'].max()}

Key Findings:
- Average Salary: ${df['salary'].mean():,.2f}
- Total Sales: ${df['sales'].sum():,.2f}
- Top Category: {df['category'].value_counts().index[0]}
"""

with open('report.txt', 'w') as f:
    f.write(report)
```

---

## Best Practices

### Performance Tips

1. **Use vectorized operations** instead of loops
2. **Avoid unnecessary copies** (use views when possible)
3. **Use appropriate data types** (category for strings, int32 vs int64)
4. **Filter early** in your pipeline
5. **Use chunking** for large files

### Code Organization

```python
# Good structure
def load_data(filepath):
    """Load and perform initial cleaning."""
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df

def analyze_sales(df):
    """Analyze sales data."""
    return df.groupby('category')['sales'].sum()

def create_visualization(data):
    """Create summary plots."""
    data.plot(kind='bar')
    plt.savefig('output.png')

# Main workflow
if __name__ == '__main__':
    df = load_data('data.csv')
    results = analyze_sales(df)
    create_visualization(results)
```

### Memory Management

```python
# For large files, use chunks
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)

# Or use specific columns
df = pd.read_csv('data.csv', usecols=['col1', 'col2', 'col3'])

# Optimize dtypes
df['category'] = df['category'].astype('category')
df['small_int'] = df['small_int'].astype('int8')
```

---

## Common Patterns

### Pattern 1: Group-Apply-Combine

```python
# Group by category, apply transformation, combine results
result = (df.groupby('category')
          .apply(lambda x: x['sales'].sum() / x['sales'].count())
          .reset_index(name='avg_sales'))
```

### Pattern 2: Method Chaining

```python
# Chain multiple operations
result = (df
          .dropna()
          .query('age > 18')
          .groupby('category')
          .agg({'sales': 'sum'})
          .sort_values('sales', ascending=False)
          .head(10))
```

### Pattern 3: Pivot Tables

```python
# Reshape data for analysis
pivot = df.pivot_table(
    values='sales',
    index='date',
    columns='category',
    aggfunc='sum'
)
```

---

## Summary

### Key Concepts

1. **NumPy**: Fast array operations, broadcasting, universal functions
2. **Pandas**: DataFrames, Series, groupby, merge operations
3. **Matplotlib**: Plotting, customization, subplots
4. **SciPy**: Statistical functions, optimization, integration
5. **Workflows**: Complete data analysis pipelines

### When to Use What

- **NumPy**: Numerical computations, array operations
- **Pandas**: Structured data, data cleaning, analysis
- **Matplotlib**: Visualizations, plots, charts
- **SciPy**: Advanced mathematics, statistics, optimization

### Next Steps

1. Practice with real datasets
2. Learn advanced Pandas techniques
3. Explore Seaborn for statistical visualization
4. Study machine learning with scikit-learn
5. Master data visualization principles
