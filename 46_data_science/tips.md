# Data Science Essentials - Tips and Best Practices

## NumPy Tips

### Performance Tips

**1. Use Vectorized Operations**

```python
import numpy as np

# SLOW: Loop
result = []
for i in range(1000000):
    result.append(i * 2)

# FAST: Vectorized
arr = np.arange(1000000)
result = arr * 2
```

Performance difference: ~100x faster with vectorization

**2. Choose Right Data Types**

```python
import numpy as np

# Use appropriate dtypes to save memory
arr_int64 = np.array([1, 2, 3], dtype=np.int64)  # 8 bytes per element
arr_int32 = np.array([1, 2, 3], dtype=np.int32)  # 4 bytes per element
arr_int8 = np.array([1, 2, 3], dtype=np.int8)    # 1 byte per element

# For boolean arrays
mask = np.array([True, False, True], dtype=bool)  # 1 byte per element
```

**3. Avoid Unnecessary Copies**

```python
# This creates a copy
arr_copy = arr.copy()

# This creates a view (points to same data)
arr_view = arr[:]
arr_view2 = arr[::2]

# Modify view affects original
arr_view[0] = 999
print(arr[0])  # 999
```

**4. Use Broadcasting Correctly**

```python
# Broadcasting allows efficient operations
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = arr + np.array([10, 20, 30])  # Adds to each row

# Without broadcasting (slow)
for i in range(arr.shape[0]):
    arr[i] = arr[i] + np.array([10, 20, 30])
```

### Common Patterns

**Pattern 1: Conditional Selection**

```python
arr = np.array([1, 2, 3, 4, 5])

# Get elements matching condition
mask = arr > 2
result = arr[mask]  # [3, 4, 5]

# Multiple conditions
result = arr[(arr > 2) & (arr < 5)]  # [3, 4]
```

**Pattern 2: Element-wise with Condition**

```python
arr = np.array([1, 2, 3, 4, 5])

# Use np.where for conditional assignment
result = np.where(arr > 2, arr * 2, arr)
# Where arr > 2: multiply by 2, else keep original
# Result: [1, 2, 6, 8, 10]
```

**Pattern 3: Aggregation Along Axis**

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum along columns (axis=1 for each row)
row_sums = arr.sum(axis=1)  # [6, 15, 24]

# Sum along rows (axis=0 for each column)
col_sums = arr.sum(axis=0)  # [12, 15, 18]

# Total sum
total = arr.sum()  # 45
```

---

## Pandas Tips

### Performance Tips

**1. Use Appropriate Data Types**

```python
import pandas as pd

# BEFORE: Uses more memory
df = pd.DataFrame({'category': ['A', 'B', 'A', 'C'] * 1000})
print(df.memory_usage(deep=True))  # ~30KB for strings

# AFTER: Convert to category
df['category'] = df['category'].astype('category')
print(df.memory_usage(deep=True))  # ~4KB

# Same for integers
df['age'] = df['age'].astype('int8')  # Instead of int64
```

**2. Read Only What You Need**

```python
# Read entire file
df = pd.read_csv('large_file.csv')  # Slow and memory intensive

# Read specific columns
df = pd.read_csv('large_file.csv', usecols=['col1', 'col2'])

# Read in chunks
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)

# Read specific rows
df = pd.read_csv('large_file.csv', skiprows=1000, nrows=10000)
```

**3. Avoid Chained Indexing**

```python
# WRONG: Chained indexing (may produce copy or view)
df['col1'][0] = 100

# RIGHT: Use loc or iloc
df.loc[0, 'col1'] = 100
df.iloc[0, 0] = 100

# RIGHT: Modify column directly
df['col1'] = df['col1'].apply(lambda x: x + 1)
```

**4. Use Method Chaining**

```python
# Chained operations are efficient
result = (df
    .dropna()
    .query('age > 18')
    .groupby('category')
    .agg({'sales': 'sum'})
    .sort_values('sales', ascending=False))
```

### Common Patterns

**Pattern 1: Group-Apply-Combine**

```python
# Calculate mean of group divided by total mean
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C'],
    'value': [10, 20, 30, 40, 50]
})

result = df.groupby('category')['value'].mean() / df['value'].mean()
```

**Pattern 2: Transform Within Groups**

```python
# Standardize values within each group
df['value_standardized'] = df.groupby('category')['value'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

**Pattern 3: Add Rank Within Groups**

```python
# Rank by value within category
df['rank'] = df.groupby('category')['value'].rank(ascending=False)
```

**Pattern 4: Window Functions**

```python
# Calculate rolling mean
df['rolling_mean'] = df['value'].rolling(window=3).mean()

# Calculate cumulative sum
df['cumsum'] = df['value'].cumsum()

# Calculate percentage change
df['pct_change'] = df['value'].pct_change()
```

### Debugging Tips

**1. Use head() and tail()**

```python
# Always check first and last rows
print(df.head())
print(df.tail())

# Check with sample
print(df.sample(5))
```

**2. Use info() for Overview**

```python
df.info()  # Shows dtypes, non-null counts
df.describe()  # Shows statistics
```

**3. Check for Missing Values**

```python
# Count missing per column
print(df.isnull().sum())

# Percentage missing
print(df.isnull().sum() / len(df) * 100)
```

**4. Verify Data Types**

```python
# Check dtypes
print(df.dtypes)

# Convert if needed
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')
```

---

## Matplotlib Tips

### Customization Tips

**1. Use Consistent Style**

```python
import matplotlib.pyplot as plt

# Set style globally
plt.style.use('seaborn-v0_8-darkgrid')

# Or set individual parameters
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10
plt.rcParams['lines.linewidth'] = 2
```

**2. Create Multiple Subplots Efficiently**

```python
# Create 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Access each subplot
axes[0, 0].plot(...)
axes[0, 1].plot(...)
axes[1, 0].plot(...)
axes[1, 1].plot(...)

# Use tight_layout to avoid overlap
plt.tight_layout()
```

**3. Save High Quality Figures**

```python
plt.savefig('figure.png', dpi=300, bbox_inches='tight')
plt.savefig('figure.pdf', dpi=300, bbox_inches='tight')
```

### Common Patterns

**Pattern 1: Add Value Labels to Bar Plot**

```python
bars = plt.bar(['A', 'B', 'C'], [10, 20, 15])
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom')
```

**Pattern 2: Dual Axis Plot**

```python
fig, ax1 = plt.subplots()

# First y-axis
ax1.plot(x, y1, 'b-')
ax1.set_ylabel('Y1', color='b')

# Second y-axis
ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Y2', color='r')
```

**Pattern 3: Heatmap**

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(5, 5)
plt.imshow(data, cmap='viridis', aspect='auto')
plt.colorbar()
plt.title('Heatmap')
```

---

## Data Workflow Tips

### The Data Analysis Pipeline

```
1. LOAD → 2. EXPLORE → 3. CLEAN → 4. TRANSFORM → 5. ANALYZE → 6. VISUALIZE → 7. REPORT
```

**Step 1: Load Thoughtfully**

```python
# Check file size first
import os
file_size = os.path.getsize('data.csv')
print(f"File size: {file_size / 1e6:.2f} MB")

# Read with caution
df = pd.read_csv('data.csv', nrows=10)  # Check first 10 rows
```

**Step 2: Explore Thoroughly**

```python
print("Shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nFirst rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nBasic statistics:")
print(df.describe())
print("\nDuplicate rows:", df.duplicated().sum())
```

**Step 3: Clean Systematically**

```python
# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()  # or fillna(strategy)

# Remove outliers
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['column'] >= Q1 - 1.5*IQR) & (df['column'] <= Q3 + 1.5*IQR)]

# Fix data types
df['date'] = pd.to_datetime(df['date'])
```

**Step 4: Transform Appropriately**

```python
# Create features
df['year'] = df['date'].dt.year
df['log_value'] = np.log(df['value'])
df['normalized'] = (df['value'] - df['value'].mean()) / df['value'].std()

# Create categories
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100])
```

**Step 5: Analyze Systematically**

```python
# Group and aggregate
results = df.groupby('category').agg({
    'value': ['mean', 'std', 'count'],
    'price': 'sum'
})

# Calculate correlations
corr = df.corr()

# Statistical tests
from scipy import stats
t_stat, p_value = stats.ttest_ind(group1, group2)
```

**Step 6: Visualize Clearly**

```python
# Create multiple visualizations
fig, axes = plt.subplots(2, 2)

# Distribution
df['value'].hist(ax=axes[0, 0])

# Correlation
import seaborn as sns
sns.heatmap(df.corr(), ax=axes[0, 1])

# Trends
df.groupby('date')['sales'].sum().plot(ax=axes[1, 0])

# Comparison
df.boxplot(by='category', ax=axes[1, 1])
```

### Memory Management

**Check Memory Usage**

```python
# See memory for each column
print(df.memory_usage(deep=True))

# Total memory
print(f"Total: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
```

**Optimize Memory**

```python
# Convert object to category if possible
df['category'] = df['category'].astype('category')

# Use smaller int type
df['age'] = df['age'].astype('uint8')

# Sparse arrays for lots of zeros
df_sparse = df.astype(pd.SparseDtype('int', 0))
```

---

## Common Pitfalls

### NumPy Pitfalls

1. **Forgetting to import** - Always `import numpy as np`
2. **Mixing Python lists with NumPy** - Convert to array first
3. **In-place vs returning** - `sort()` modifies in-place, `sorted()` returns new
4. **Index starting at 0** - Python uses 0-based indexing
5. **Broadcasting confusion** - Check shapes when operations fail

### Pandas Pitfalls

1. **Index alignment** - Operations align by index, not position
2. **SettingWithCopyWarning** - Use `.copy()` when needed
3. **In-place operations** - Not all operations have `inplace=True`
4. **Chained indexing** - Use `.loc[]` or `.iloc[]` explicitly
5. **NaN handling** - Many functions skip NaN by default

### Matplotlib Pitfalls

1. **Forgetting plt.show()** - Nothing displays without it
2. **Figure not clearing** - Use `plt.clf()` or create new figure
3. **Overlapping text** - Use `plt.tight_layout()`
4. **Wrong axis** - Remember axis=0 is rows, axis=1 is columns
5. **Color map limits** - Set `vmin` and `vmax` for consistent scaling

---

## Performance Checklist

Before deploying analysis:

- [ ] Tested with full dataset
- [ ] Memory usage is acceptable
- [ ] Execution time is reasonable
- [ ] No SettingWithCopyWarnings
- [ ] All data types are appropriate
- [ ] Missing values handled appropriately
- [ ] Outliers checked and handled
- [ ] Results validated against manual calculations
- [ ] Code is readable and documented
- [ ] Visualizations are clear and labeled

---

## Resources

- NumPy docs: https://numpy.org/doc/
- Pandas docs: https://pandas.pydata.org/docs/
- Matplotlib docs: https://matplotlib.org/stable/contents.html
- SciPy docs: https://docs.scipy.org/
- Real Python tutorials: https://realpython.com/
