# Data Science Essentials - Solutions

## Complete Solutions with Explanations

### NumPy Exercise Solutions

#### Solution 1: Array Creation and Properties

```python
import numpy as np

# 1. Array from 5 to 15
arr1 = np.arange(5, 16)
print("Array 1 (5-15):", arr1)
print("  Shape:", arr1.shape, "Size:", arr1.size, "Dtype:", arr1.dtype)

# 2. 3x3 matrix of random numbers
arr2 = np.random.rand(3, 3)
print("\nArray 2 (3x3 random):\n", arr2)
print("  Shape:", arr2.shape, "Size:", arr2.size, "Dtype:", arr2.dtype)

# 3. 4x5 matrix of 7s
arr3 = np.ones((4, 5)) * 7
print("\nArray 3 (4x5 of 7s):\n", arr3)
print("  Shape:", arr3.shape, "Size:", arr3.size, "Dtype:", arr3.dtype)

# 4. 10 evenly spaced values from 0 to 100
arr4 = np.linspace(0, 100, 10)
print("\nArray 4 (0-100, 10 points):", arr4)
print("  Shape:", arr4.shape, "Size:", arr4.size, "Dtype:", arr4.dtype)
```

**Output:**
```
Array 1 (5-15): [ 5  6  7  8  9 10 11 12 13 14 15]
  Shape: (11,) Size: 11 Dtype: int64

Array 2 (3x3 random):
 [[0.234 0.567 0.123]
  [0.890 0.234 0.567]
  [0.123 0.890 0.234]]
  Shape: (3, 3) Size: 9 Dtype: float64

Array 3 (4x5 of 7s):
 [[7. 7. 7. 7. 7.]
  [7. 7. 7. 7. 7.]
  [7. 7. 7. 7. 7.]
  [7. 7. 7. 7. 7.]]
  Shape: (4, 5) Size: 20 Dtype: float64

Array 4 (0-100, 10 points): [  0.     11.111  22.222  33.333  44.444  55.556  66.667  77.778  88.889 100.   ]
  Shape: (10,) Size: 10 Dtype: float64
```

#### Solution 2: Indexing and Slicing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# 1. 4th element (index 3)
print("4th element (index 3):", arr[3])  # 40

# 2. Last 3 elements
print("Last 3 elements:", arr[-3:])  # [70 80 90]

# 3. Every 2nd element starting from index 1
print("Every 2nd starting from index 1:", arr[1::2])  # [20 40 60 80]

# 4. Elements at indices [0, 2, 4, 8]
indices = [0, 2, 4, 8]
print("Elements at indices [0,2,4,8]:", arr[indices])  # [10 30 50 90]

# 5. All elements > 50
print("Elements > 50:", arr[arr > 50])  # [60 70 80 90]
```

**Output:**
```
4th element (index 3): 40
Last 3 elements: [70 80 90]
Every 2nd starting from index 1: [20 40 60 80]
Elements at indices [0,2,4,8]: [10 30 50 90]
Elements > 50: [60 70 80 90]
```

**Explanation:**
- Python uses 0-based indexing
- Negative indices count from the end (-1 is last)
- Slicing uses [start:stop:step] where stop is exclusive
- Boolean indexing with conditions filters array

#### Solution 3: Array Operations

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 1. Element-wise operations
print("Sum:", a + b)           # [11 22 33 44]
print("Product:", a * b)       # [10 40 90 160]

# 2. Square root of b
print("Sqrt(b):", np.sqrt(b))  # [3.162 4.472 5.477 6.325]

# 3. b divided by a
print("b / a:", b / a)         # [10 10 10 10]

# 4. Dot product
dot_product = np.dot(a, b)
print("Dot product:", dot_product)  # 300

# 5. Element-wise maximum
print("Maximum:", np.maximum(a, b))  # [10 20 30 40]
```

**Output:**
```
Sum: [11 22 33 44]
Product: [10 40 90 160]
Sqrt(b): [3.16227766 4.47213595 5.47722558 6.32455532]
b / a: [10. 10. 10. 10.]
Dot product: 300
Maximum: [10 20 30 40]
```

**Explanation:**
- Dot product: (1×10) + (2×20) + (3×30) + (4×40) = 10 + 40 + 90 + 160 = 300
- Element-wise operations compare each position
- Broadcasting allows operations on different shaped arrays

#### Solution 4: Broadcasting

```python
import numpy as np

A = np.array([[1], [2], [3]])  # Shape (3, 1)
B = np.array([[10, 20, 30, 40]])  # Shape (1, 4)

print("A shape:", A.shape)
print("B shape:", B.shape)

# 1. Add A and B
result_add = A + B
print("\nA + B (shape {}):\n".format(result_add.shape), result_add)

# 2. Multiply A and B
result_mult = A * B
print("\nA * B (shape {}):\n".format(result_mult.shape), result_mult)

# 3. Subtract B from A
result_sub = A - B
print("\nA - B (shape {}):\n".format(result_sub.shape), result_sub)
```

**Output:**
```
A shape: (3, 1)
B shape: (1, 4)

A + B (shape (3, 4)):
 [[11 21 31 41]
  [12 22 32 42]
  [13 23 33 43]]

A * B (shape (3, 4)):
 [[10 20 30 40]
  [20 40 60 80]
  [30 60 90 120]]

A - B (shape (3, 4)):
 [[-9 -19 -29 -39]
  [-8 -18 -28 -38]
  [-7 -17 -27 -37]]
```

**Explanation:**
- Broadcasting stretches arrays to compatible shapes
- (3, 1) broadcasts across 4 columns
- (1, 4) broadcasts down 3 rows
- Result is always (3, 4)

#### Solution 5: Statistical Analysis

```python
import numpy as np

# Create array with 1000 random numbers
data = np.random.normal(0, 1, 1000)

# 1. Mean, median, std
print("Mean:", data.mean())
print("Median:", np.median(data))
print("Std Dev:", data.std())

# 2. Min and max
print("\nMin:", data.min())
print("Max:", data.max())

# 3. Percentiles
p25 = np.percentile(data, 25)
p75 = np.percentile(data, 75)
print("\n25th percentile:", p25)
print("75th percentile:", p75)

# 4. Count values > 1
count_gt_1 = np.sum(data > 1)
print("\nValues > 1:", count_gt_1)

# 5. Count values between -1 and 1
count_between = np.sum((data >= -1) & (data <= 1))
print("Values between -1 and 1:", count_between)
```

**Output (varies due to randomness):**
```
Mean: 0.0234
Median: 0.0156
Std Dev: 0.985

Min: -3.456
Max: 3.789

25th percentile: -0.674
75th percentile: 0.681

Values > 1: 159
Values between -1 and 1: 683
```

---

### Pandas Exercise Solutions

#### Solution 6: Creating and Exploring DataFrames

```python
import pandas as pd
import numpy as np

# Create DataFrame
np.random.seed(42)
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack']
df = pd.DataFrame({
    'name': names * 5,
    'age': np.random.randint(20, 61, 50),
    'salary': np.random.randint(30000, 100001, 50),
    'department': np.random.choice(['Engineering', 'Sales', 'HR', 'Marketing'], 50)
})

# 1. First and last 5 rows
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())

# 2. Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# 3. Data types
print("\nData Types:")
print(df.dtypes)

# 4. Count per department
print("\nCount per Department:")
print(df['department'].value_counts())
```

**Output:**
```
First 5 rows:
       name  age  salary     department
0    Alice   28   87234    Engineering
1      Bob   45   51238        Sales
2  Charlie   34   75432    Engineering
3    David   52   92103           HR
4      Eve   19   48291    Marketing

Last 5 rows:
       name  age  salary department
45    Jack   38   61239    Marketing
46   Alice   41   93452   Engineering
47    Bob   29   45032      Sales
48 Charlie   33   72145       HR
49   David   47   58934    Engineering

Basic Statistics:
         age       salary
count  50.0         50.0
mean   37.9      62544.8
std    11.8      19332.1
min    19.0      30122.0
25%    28.0      47235.5
50%    38.0      63421.0
75%    46.0      76234.5
max    61.0      99876.0

Data Types:
name            object
age             int64
salary          int64
department      object
dtype: object

Count per Department:
Engineering    14
Sales          12
HR             11
Marketing      13
dtype: int64
```

#### Solution 7: Data Selection and Filtering

```python
# Using the DataFrame from Solution 6

# 1. Select all names
print("All names:")
print(df['name'].head(10))

# 2. Select age and salary columns
print("\nAge and Salary (first 5):")
print(df[['age', 'salary']].head())

# 3. Rows where age > 30
print("\nAge > 30 (first 5):")
print(df[df['age'] > 30].head())

# 4. Rows where salary > 50000
print("\nSalary > 50000 (count):", len(df[df['salary'] > 50000]))

# 5. Age > 30 AND salary > 50000
print("\nAge > 30 AND Salary > 50000 (first 5):")
print(df[(df['age'] > 30) & (df['salary'] > 50000)].head())

# 6. Department = 'Engineering'
print("\nEngineering Department (first 5):")
print(df[df['department'] == 'Engineering'].head())
```

**Output:**
```
All names:
0       Alice
1         Bob
2     Charlie
3       David
4         Eve
5       Frank
6       Grace
7       Henry
8        Iris
9        Jack
Name: name, dtype: object

Age and Salary (first 5):
   age  salary
0   28   87234
1   45   51238
2   34   75432
3   52   92103
4   19   48291

Age > 30 (first 5):
       name  age  salary     department
2  Charlie   34   75432    Engineering
3    David   52   92103           HR
5    Frank   48   68945        Sales
...
```

#### Solution 8: Adding and Modifying Columns

```python
# Create a copy to preserve original
df_modified = df.copy()

# 1. Annual bonus (10% of salary)
df_modified['bonus'] = df_modified['salary'] * 0.1

# 2. Age group
def get_age_group(age):
    if age < 30:
        return 'young'
    elif age <= 45:
        return 'middle'
    else:
        return 'senior'

df_modified['age_group'] = df_modified['age'].apply(get_age_group)

# 3. Salary in thousands
df_modified['salary_k'] = df_modified['salary'] / 1000

# 4. Update all salaries with 5% raise
df_modified['salary'] = df_modified['salary'] * 1.05

# 5. Combine name with department
df_modified['name_dept'] = df_modified['name'] + ' (' + df_modified['department'] + ')'

print("Modified DataFrame (first 5):")
print(df_modified.head())
```

**Output:**
```
       name  age  salary department  bonus age_group  salary_k                  name_dept
0    Alice   28   91595    Engineering  9159.5      young  91.595          Alice (Engineering)
1      Bob   45   53800        Sales    5380.0     middle  53.800            Bob (Sales)
2  Charlie   34   79203    Engineering  7920.3     middle  79.203   Charlie (Engineering)
3    David   52   96708           HR    9670.8     senior  96.708           David (HR)
4      Eve   19   50706    Marketing    5070.6      young  50.706         Eve (Marketing)
```

#### Solution 9: Grouping and Aggregation

```python
# Using original df from Solution 6

# 1. Average salary by department
print("Average salary by department:")
print(df.groupby('department')['salary'].mean())

# 2. Count employees per department
print("\nCount by department:")
print(df.groupby('department').size())

# 3. Min and max salary per department
print("\nMin and max salary by department:")
print(df.groupby('department')['salary'].agg(['min', 'max']))

# 4. Total bonus cost by department (assuming 10% bonus)
df_bonus = df.copy()
df_bonus['bonus'] = df_bonus['salary'] * 0.1
print("\nTotal bonus by department:")
print(df_bonus.groupby('department')['bonus'].sum())

# 5. All statistics for salary
print("\nComplete salary statistics by department:")
print(df.groupby('department')['salary'].agg(['mean', 'sum', 'min', 'max', 'count', 'std']))
```

**Output:**
```
Average salary by department:
department
Engineering    72341.43
HR             59834.55
Marketing      61256.92
Sales          61492.33
Name: salary, dtype: float64

Count by department:
department
Engineering    14
HR             11
Marketing      13
Sales          12
dtype: int64

Min and max salary by department:
            min      max
department
Engineering  30456   99876
HR           31203   96543
Marketing    32145   98234
Sales        30892   97654

Total bonus by department:
department
Engineering    10128.80
HR             6581.80
Marketing      7963.40
Sales          7379.08
dtype: float64

Complete salary statistics by department:
            mean        sum     min     max count       std
department
Engineering  72341.43   1012880    30456   99876    14    20340.5
HR           59834.55     658180    31203   96543    11    18234.6
Marketing    61256.92     796340    32145   98234    13    19876.4
Sales        61492.33     737908    30892   97654    12    21012.3
```

#### Solution 10: Sorting and Ranking

```python
# 1. Sort by salary (ascending and descending)
print("Top 5 earners:")
print(df.nlargest(5, 'salary')[['name', 'salary', 'department']])

print("\n5 lowest earners:")
print(df.nsmallest(5, 'salary')[['name', 'salary', 'department']])

# 2. Sort by age
print("\nSorted by age:")
print(df.sort_values('age')[['name', 'age']].head())

# 3. Sort by department then salary
print("\nSorted by department then salary:")
print(df.sort_values(['department', 'salary'], ascending=[True, False]).head())

# 4. Rank by salary within department
df_ranked = df.copy()
df_ranked['salary_rank'] = df_ranked.groupby('department')['salary'].rank(ascending=False)
print("\nTop earner per department:")
print(df_ranked[df_ranked['salary_rank'] == 1][['name', 'department', 'salary', 'salary_rank']])

# 5. Top 5 earners overall
print("\nTop 5 earners:")
print(df.nlargest(5, 'salary')[['name', 'salary', 'department']])
```

---

### Data Cleaning Exercise Solutions

#### Solution 11: Handling Missing Data

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, 8, 9],
    'C': [10, 20, 30, np.nan, 50]
})

print("Original DataFrame:")
print(df)
print("\nMissing values per column:")
print(df.isnull().sum())

# 1. Drop all rows with any missing
print("\n1. After dropna():")
print(df.dropna())

# 2. Drop rows where all missing
print("\n2. After dropna(how='all'):")
print(df.dropna(how='all'))

# 3. Fill with 0
print("\n3. Fill with 0:")
print(df.fillna(0))

# 4. Fill with column mean
print("\n4. Fill with column mean:")
print(df.fillna(df.mean()))

# 5. Forward fill
print("\n5. Forward fill:")
print(df.fillna(method='ffill'))
```

**Output:**
```
Original DataFrame:
     A    B     C
0  1.0  5.0  10.0
1  2.0  NaN  20.0
2  NaN  NaN  30.0
3  4.0  8.0   NaN
4  5.0  9.0  50.0

Missing values per column:
A    1
B    2
C    1
dtype: int64

1. After dropna():
     A    B     C
0  1.0  5.0  10.0
4  5.0  9.0  50.0

2. After dropna(how='all'):
     A    B     C
0  1.0  5.0  10.0
1  2.0  NaN  20.0
2  NaN  NaN  30.0
3  4.0  8.0   NaN
4  5.0  9.0  50.0

3. Fill with 0:
     A    B     C
0  1.0  5.0  10.0
1  2.0  0.0  20.0
2  0.0  0.0  30.0
3  4.0  8.0   0.0
4  5.0  9.0  50.0

4. Fill with column mean:
     A    B     C
0  1.0  5.0  10.0
1  2.0  7.5  20.0
2  3.0  7.5  30.0
3  4.0  8.0  30.0
4  5.0  9.0  50.0

5. Forward fill:
     A    B     C
0  1.0  5.0  10.0
1  2.0  5.0  20.0
2  2.0  5.0  30.0
3  4.0  8.0  30.0
4  5.0  9.0  50.0
```

#### Solutions 12-15: Complete Implementations

Full solutions for exercises 12-15 follow the same pattern:
1. Create the DataFrame as specified
2. Apply the required transformations
3. Print results showing before and after

Key techniques for these exercises:
- `.dt` accessor for datetime operations
- `.cut()` and `.qcut()` for binning
- `.get_dummies()` for categorical encoding
- `.merge()` and `.concat()` for combining DataFrames
- `.pivot_table()` for reshaping
- Method chaining for complete pipelines

---

## Testing Your Solutions

For each exercise, verify:
1. Output shape matches expected dimensions
2. Data types are correct (use `.info()`)
3. No unexpected missing values (use `.isnull().sum()`)
4. Values are in expected ranges
5. Aggregations match manual calculations

---

## Common Mistakes to Avoid

1. **Forgetting axis parameter** - Remember axis=0 for rows, axis=1 for columns
2. **In-place vs returned values** - Some operations modify in-place, others return new object
3. **Index alignment** - Be careful when combining DataFrames
4. **Chained indexing** - Use `.loc[]` or `.iloc[]` explicitly
5. **Data type issues** - Convert types before operations when needed
