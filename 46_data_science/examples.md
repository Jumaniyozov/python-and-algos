# Data Science Essentials - Examples

## 15 Practical, Runnable Examples

### NumPy Examples

#### Example 1: Creating and Manipulating Arrays

```python
import numpy as np

# Create different types of arrays
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

print("1D array:", arr1d)
print("2D array shape:", arr2d.shape)
print("Zeros:\n", zeros)
print("Range:", range_arr)
print("Linspace:", linspace_arr)

# Reshaped array
reshaped = arr1d.reshape(5, 1)
print("Reshaped:\n", reshaped)
```

**Output:**
```
1D array: [1 2 3 4 5]
2D array shape: (3, 3)
Zeros:
 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]
Range: [0 2 4 6 8]
Linspace: [0.   0.25 0.5  0.75 1.  ]
```

#### Example 2: NumPy Indexing and Slicing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 1D indexing
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Middle slice:", arr[2:5])
print("Every 2nd element:", arr[::2])

# 2D indexing
print("\nFirst row:", arr2d[0])
print("Last column:", arr2d[:, -1])
print("Subarray:\n", arr2d[0:2, 1:3])

# Boolean indexing
print("\nElements > 30:", arr[arr > 30])
print("Even elements:", arr[arr % 2 == 0])
```

**Output:**
```
First element: 10
Last element: 80
Middle slice: [30 40 50]
Every 2nd element: [10 30 50 70]

First row: [1 2 3]
Last column: [3 6 9]
Subarray:
 [[2 3]
  [5 6]]

Elements > 30: [40 50 60 70 80]
Even elements: [10 20 30 40 50 60 70 80]
```

#### Example 3: Array Operations and Broadcasting

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Element-wise operations
print("Addition:", arr1 + 10)
print("Multiplication:", arr1 * 2)
print("Power:", arr1 ** 2)

# Array-array operations
print("\nArray addition:", arr1 + arr2)
print("Array multiplication:", arr1 * arr2)

# Broadcasting
print("\nBroadcasting example:")
print("Original 2D array:\n", arr2d)
print("Add [10, 20, 30] to each row:\n", arr2d + np.array([10, 20, 30]))

# Column broadcasting
print("Add [[10], [20]] to columns:\n", arr2d + np.array([[10], [20]]))
```

**Output:**
```
Addition: [11 12 13 14]
Multiplication: [2 4 6 8]
Power: [1 4 9 16]

Array addition: [11 22 33 44]
Array multiplication: [10 40 90 160]

Broadcasting example:
Original 2D array:
 [[1 2 3]
  [4 5 6]]
Add [10, 20, 30] to each row:
 [[11 22 33]
  [14 25 36]]
Add [[10], [20]] to columns:
 [[11 12 13]
  [24 25 26]]
```

#### Example 4: Statistical Operations

```python
import numpy as np

data = np.array([3, 7, 2, 9, 1, 5, 8, 4, 6])
data2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic statistics
print("Sum:", data.sum())
print("Mean:", data.mean())
print("Median:", np.median(data))
print("Std Dev:", data.std())
print("Min:", data.min())
print("Max:", data.max())

# Along axis
print("\n2D array:\n", data2d)
print("Sum along rows (axis=1):", data2d.sum(axis=1))
print("Sum along columns (axis=0):", data2d.sum(axis=0))
print("Mean along columns:", data2d.mean(axis=0))

# Unique values and counts
arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique, counts = np.unique(arr, return_counts=True)
print("\nUnique values:", unique)
print("Counts:", counts)
```

**Output:**
```
Sum: 45
Mean: 5.0
Median: 5.0
Std Dev: 2.5819888974716112
Min: 1
Max: 9

2D array:
 [[1 2 3]
  [4 5 6]
  [7 8 9]]
Sum along rows (axis=1): [ 6 15 24]
Sum along columns (axis=0): [12 15 18]
Mean along columns: [4. 5. 6.]

Unique values: [1 2 3 4]
Counts: [1 2 3 4]
```

#### Example 5: Matrix Operations

```python
import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)  # or A @ B
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nA dot B:\n", C)

# Transpose
print("\nTranspose of A:\n", A.T)

# Determinant
from numpy.linalg import det
print("Determinant of A:", det(A))

# Inverse
from numpy.linalg import inv
A_inv = inv(A)
print("\nInverse of A:\n", A_inv)

# Verify: A @ A_inv = I
print("\nA @ A^-1:\n", np.dot(A, A_inv))
```

**Output:**
```
Matrix A:
 [[1 2]
 [3 4]]

Matrix B:
 [[5 6]
 [7 8]]

A dot B:
 [[19 22]
 [43 50]]

Transpose of A:
 [[1 3]
 [2 4]]

Determinant of A: -2.0

Inverse of A:
 [[-2.   1. ]
  [ 1.5 -0.5]]

A @ A^-1:
 [[1. 0.]
 [0. 1.]]
```

---

### Pandas Examples

#### Example 6: Creating and Exploring DataFrames

```python
import pandas as pd
import numpy as np

# Create DataFrame from dictionary
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 65000],
    'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales']
})

print("DataFrame:")
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())
print("\nColumn names:", df.columns.tolist())
print("Shape:", df.shape)
print("Index:", df.index.tolist())
```

**Output:**
```
         name  age  salary     department
0      Alice   25   50000   Engineering
1        Bob   30   60000        Sales
2    Charlie   35   75000   Engineering
3      David   28   55000           HR
4        Eve   32   65000        Sales

DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype
--- ------      --------------  -----
 0   name        5 non-null      object
 1   age         5 non-null      int64
 2   salary      5 non-null      int64
 3   department  5 non-null      object
dtypes: int64(2), object(2)

Basic Statistics:
          age       salary
count    5.0         5.0
mean    30.0    61000.0
std      4.1     10295.7
min     25.0    50000.0
25%     28.0    55000.0
50%     30.0    60000.0
75%     32.0    65000.0
max     35.0    75000.0

Column names: ['name', 'age', 'salary', 'department']
Shape: (5, 4)
Index: [0, 1, 2, 3, 4]
```

#### Example 7: Selecting and Filtering Data

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 65000]
})

# Select columns
print("Single column:")
print(df['name'])
print("\nMultiple columns:")
print(df[['name', 'age']])

# Select rows by label
print("\nRow 0 (loc):")
print(df.loc[0])

# Select rows by position
print("\nFirst 3 rows (iloc):")
print(df.iloc[:3])

# Boolean filtering
print("\nAge > 28:")
print(df[df['age'] > 28])

# Multiple conditions
print("\nAge > 28 AND salary < 65000:")
print(df[(df['age'] > 28) & (df['salary'] < 65000)])

# isin() method
print("\nNames in ['Alice', 'David']:")
print(df[df['name'].isin(['Alice', 'David'])])
```

**Output:**
```
Single column:
0      Alice
1        Bob
2    Charlie
3      David
4        Eve
Name: name, dtype: object

Multiple columns:
       name  age
0    Alice   25
1      Bob   30
2  Charlie   35
3    David   28
4      Eve   32

Row 0 (loc):
name      Alice
age          25
salary    50000
Name: 0, dtype: object

First 3 rows (iloc):
       name  age  salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   75000

Age > 28:
       name  age  salary
1      Bob   30   60000
2  Charlie   35   75000
4      Eve   32   65000

Age > 28 AND salary < 65000:
    name  age  salary
1    Bob   30   60000

Names in ['Alice', 'David']:
     name  age  salary
0   Alice   25   50000
3   David   28   55000
```

#### Example 8: Data Manipulation

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 65000]
})

# Add new column
df['salary_k'] = df['salary'] / 1000
print("After adding salary_k:")
print(df)

# Apply function to column
df['age_group'] = df['age'].apply(lambda x: 'young' if x < 30 else 'senior')
print("\nAfter adding age_group:")
print(df)

# Modify column
df['salary'] = df['salary'].apply(lambda x: x * 1.1)  # 10% raise
print("\nAfter 10% raise:")
print(df[['name', 'salary']])

# Drop column
df_dropped = df.drop('salary_k', axis=1)
print("\nAfter dropping salary_k:")
print(df_dropped.head(2))

# Rename columns
df_renamed = df.rename(columns={'name': 'employee_name', 'age': 'years_old'})
print("\nRenamed columns:", df_renamed.columns.tolist())
```

**Output:**
```
After adding salary_k:
       name  age  salary  salary_k
0    Alice   25   50000       50.0
1      Bob   30   60000       60.0
2  Charlie   35   75000       75.0
3    David   28   55000       55.0
4      Eve   32   65000       65.0

After adding age_group:
       name  age  salary salary_k age_group
0    Alice   25   50000       50.0      young
1      Bob   30   60000       60.0     senior
2  Charlie   35   75000       75.0     senior
3    David   28   55000       55.0      young
4      Eve   32   65000       65.0     senior

After 10% raise:
       name    salary
0    Alice  55000.00
1      Bob  66000.00
2  Charlie  82500.00
3    David  60500.00
4      Eve  71500.00

After dropping salary_k:
       name  age  salary age_group
0    Alice   25   50000      young

Renamed columns: ['employee_name', 'years_old', 'salary', 'salary_k', 'age_group']
```

#### Example 9: Grouping and Aggregation

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'salary': [50000, 60000, 75000, 55000, 65000, 70000],
    'bonus': [5000, 8000, 10000, 3000, 7000, 8000]
})

# Simple groupby
print("Average salary by department:")
print(df.groupby('department')['salary'].mean())

# Multiple aggregations
print("\nSalary stats by department:")
result = df.groupby('department')['salary'].agg(['mean', 'sum', 'count', 'min', 'max'])
print(result)

# Multiple columns
print("\nMultiple aggregations:")
result = df.groupby('department').agg({
    'salary': ['mean', 'sum'],
    'bonus': 'mean'
})
print(result)

# Custom aggregation names
result = (df.groupby('department')
          .agg(avg_salary=('salary', 'mean'),
               total_bonus=('bonus', 'sum'),
               count=('name', 'count')))
print("\nNamed aggregations:")
print(result)
```

**Output:**
```
Average salary by department:
department
Engineering    65000.0
HR             55000.0
Sales          62500.0
Name: salary, dtype: float64

Salary stats by department:
            mean   sum  count   min   max
department
Engineering 65000 195000      3 50000 75000
HR          55000  55000      1 55000 55000
Sales       62500 125000      2 60000 65000

Multiple aggregations:
                salary       bonus
                  mean    sum  mean
department
Engineering   65000.0 195000  9000
HR            55000.0  55000  3000
Sales         62500.0 125000  7500

Named aggregations:
           avg_salary  total_bonus  count
department
Engineering       65000        27000      3
HR                55000         3000      1
Sales             62500        15000      2
```

#### Example 10: Handling Missing Data

```python
import pandas as pd
import numpy as np

# Create DataFrame with missing values
df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'David', 'Eve'],
    'age': [25, np.nan, 35, 28, 32],
    'salary': [50000, 60000, 75000, np.nan, 65000]
})

print("Original DataFrame:")
print(df)

# Detect missing values
print("\nMissing value counts:")
print(df.isnull().sum())

# Drop rows with any missing values
print("\nAfter dropna():")
print(df.dropna())

# Drop rows where all values are missing
print("\nAfter dropna(how='all'):")
print(df.dropna(how='all'))

# Fill with specific value
print("\nFill with 0:")
print(df.fillna(0))

# Fill with mean
print("\nFill with column mean:")
print(df.fillna(df.mean()))

# Forward fill
df_ffill = df.fillna(method='ffill')
print("\nForward fill:")
print(df_ffill)

# Interpolate
df_numeric = df[['age', 'salary']].copy()
df_interp = df_numeric.interpolate()
print("\nInterpolated:")
print(df_interp)
```

**Output:**
```
Original DataFrame:
    name   age  salary
0  Alice  25.0   50000
1    Bob   NaN   60000
2   None  35.0   75000
3  David  28.0     NaN
4    Eve  32.0   65000

Missing value counts:
name       1
age        1
salary     1
dtype: int64

After dropna():
     name   age  salary
0   Alice  25.0   50000
4     Eve  32.0   65000

After dropna(how='all'):
    name   age  salary
0  Alice  25.0   50000
1    Bob   NaN   60000
2   None  35.0   75000
3  David  28.0     NaN
4    Eve  32.0   65000

Fill with 0:
    name   age  salary
0  Alice  25.0   50000
1    Bob    0.0   60000
2      0   35.0   75000
3  David  28.0      0
4    Eve  32.0   65000

Fill with column mean:
    name     age  salary
0  Alice  25.0  50000
1    Bob  30.0  60000
2   None  35.0  75000
3  David  28.0  65000
4    Eve  32.0  65000

Forward fill:
    name   age  salary
0  Alice  25.0   50000
1    Bob  25.0   60000
2   None  35.0   75000
3  David  28.0   75000
4    Eve  32.0   65000

Interpolated:
    age  salary
0  25.0   50000
1  28.5   60000
2  35.0   75000
3  32.0   70000
4  32.0   65000
```

---

### Matplotlib Examples

#### Example 11: Basic Line and Scatter Plots

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

# Line plot
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1, 'b-', label='sin(x)', linewidth=2)
plt.plot(x, y2, 'r--', label='cos(x)', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True, alpha=0.3)

# Scatter plot
plt.subplot(1, 2, 2)
plt.scatter(x, y1, color='blue', s=50, alpha=0.6, label='sin(x)')
plt.scatter(x, y2, color='red', s=50, alpha=0.6, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

#### Example 12: Bar and Histogram Plots

```python
import matplotlib.pyplot as plt
import numpy as np

# Bar plot
categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
popularity = [95, 85, 80, 70, 65]

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
bars = plt.bar(categories, popularity, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
plt.ylabel('Popularity Score')
plt.title('Programming Language Popularity')
plt.ylim(0, 100)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom')

# Histogram
plt.subplot(1, 2, 2)
data = np.random.normal(100, 15, 1000)
plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution (Normal)')
plt.axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.1f}')
plt.legend()

plt.tight_layout()
plt.show()
```

#### Example 13: Subplots and Multi-plot Layouts

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1: Line plot
axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
axes[0, 0].set_title('sin(x)')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Cosine
axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
axes[0, 1].set_title('cos(x)')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Exponential
axes[1, 0].plot(x, np.exp(x/5), 'g-', linewidth=2)
axes[1, 0].set_title('exp(x/5)')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Combined
axes[1, 1].plot(x, np.sin(x), label='sin(x)')
axes[1, 1].plot(x, np.cos(x), label='cos(x)')
axes[1, 1].set_title('Combined')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.suptitle('Trigonometric Functions', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

#### Example 14: Integration with Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [10000, 12000, 15000, 14000, 18000, 20000],
    'Profit': [2000, 2500, 3500, 3000, 4000, 4500]
})

plt.figure(figsize=(12, 5))

# Line plot
plt.subplot(1, 2, 1)
df.plot(x='Month', y=['Sales', 'Profit'], ax=plt.gca(), marker='o')
plt.title('Sales and Profit by Month')
plt.ylabel('Amount ($)')

# Bar plot
plt.subplot(1, 2, 2)
df.set_index('Month')[['Sales', 'Profit']].plot(kind='bar', ax=plt.gca())
plt.title('Sales and Profit Comparison')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

#### Example 15: Advanced Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

# Create figure with different plot types
fig = plt.figure(figsize=(14, 8))

# 1. Pie chart
ax1 = plt.subplot(2, 3, 1)
sizes = [30, 25, 20, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Pie Chart')

# 2. Box plot
ax2 = plt.subplot(2, 3, 2)
data = [np.random.normal(100, 10, 100),
        np.random.normal(110, 12, 100),
        np.random.normal(105, 15, 100)]
ax2.boxplot(data, labels=['Group A', 'Group B', 'Group C'])
ax2.set_ylabel('Values')
ax2.set_title('Box Plot')

# 3. Contour plot
ax3 = plt.subplot(2, 3, 3)
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
contour = ax3.contourf(X, Y, Z, levels=10, cmap='viridis')
ax3.set_title('Contour Plot')
plt.colorbar(contour, ax=ax3)

# 4. Heatmap
ax4 = plt.subplot(2, 3, 4)
data = np.random.rand(5, 5)
im = ax4.imshow(data, cmap='hot', aspect='auto')
ax4.set_title('Heatmap')
plt.colorbar(im, ax=ax4)

# 5. Histogram with KDE
ax5 = plt.subplot(2, 3, 5)
data = np.random.normal(0, 1, 1000)
ax5.hist(data, bins=30, density=True, alpha=0.7, edgecolor='black')
from scipy import stats
x = np.linspace(-4, 4, 100)
ax5.plot(x, stats.norm.pdf(x), 'r-', linewidth=2, label='Normal PDF')
ax5.set_title('Histogram with PDF')
ax5.legend()

# 6. Scatter with color scale
ax6 = plt.subplot(2, 3, 6)
x = np.random.randn(100)
y = np.random.randn(100)
colors = x + y
scatter = ax6.scatter(x, y, c=colors, s=50, cmap='cool', alpha=0.6)
ax6.set_title('Scatter with Color Scale')
plt.colorbar(scatter, ax=ax6)

plt.suptitle('Advanced Matplotlib Visualizations', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Example Patterns

### Data Loading and Exploration Pattern

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Explore
print(df.head())
print(df.info())
print(df.describe())

# Visualize
df.hist(figsize=(10, 8))
plt.show()
```

### Data Cleaning Pattern

```python
# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(df.mean())  # or dropna()

# Data type conversion
df['date'] = pd.to_datetime(df['date'])

# Outlier removal
df = df[np.abs(df['value'] - df['value'].mean()) <= (3 * df['value'].std())]
```

### Analysis Pipeline Pattern

```python
result = (df
    .dropna()
    .query('age > 18')
    .groupby('category')
    .agg({'sales': 'sum'})
    .sort_values('sales', ascending=False)
    .head(10))
```

---

## Key Takeaways

1. **NumPy**: Use for numerical operations, arrays, and mathematical functions
2. **Pandas**: Use for data manipulation, cleaning, and analysis
3. **Matplotlib**: Use for creating visualizations
4. **Integration**: All three work seamlessly together
5. **Efficiency**: Vectorized operations are much faster than loops
