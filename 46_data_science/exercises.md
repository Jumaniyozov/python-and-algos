# Data Science Essentials - Exercises

## 15 Progressive Challenges

### NumPy Exercises

#### Exercise 1: Array Creation and Properties

Create arrays with the following specifications:
1. A 1D array with integers from 5 to 15
2. A 3x3 matrix of random numbers between 0 and 1
3. A 4x5 matrix filled with 7s
4. A 1D array with 10 evenly spaced values from 0 to 100

Then print the shape, size, and dtype of each array.

**Hint:** Use `np.arange()`, `np.random.rand()`, `np.ones()`, and `np.linspace()`

#### Exercise 2: Indexing and Slicing

Given array `arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])`:
1. Extract the 4th element (index 3)
2. Extract the last 3 elements
3. Extract every 2nd element starting from index 1
4. Extract elements at indices [0, 2, 4, 8]
5. Extract all elements greater than 50

**Hint:** Use standard indexing, slicing, and boolean indexing

#### Exercise 3: Array Operations

Create two arrays: `a = np.array([1, 2, 3, 4])` and `b = np.array([10, 20, 30, 40])`

Compute:
1. Element-wise sum and product
2. Square root of elements in `b`
3. `b` divided by `a`
4. The dot product of `a` and `b`
5. Element-wise maximum between `a` and `b`

**Hint:** Use `np.sqrt()`, `np.dot()`, `np.maximum()`

#### Exercise 4: Broadcasting

Create array `A` with shape (3, 1) filled with [1, 2, 3] and array `B` with shape (1, 4) filled with [10, 20, 30, 40].

1. Add `A` and `B` (result should be 3x4)
2. Multiply `A` and `B` (result should be 3x4)
3. Subtract `B` from `A` (result should be 3x4)

Print the resulting shapes and values.

**Hint:** Use reshape() if needed

#### Exercise 5: Statistical Analysis

Create an array with 1000 random numbers from a normal distribution (mean=0, std=1).

Calculate:
1. Mean, median, and standard deviation
2. Min and max values
3. 25th and 75th percentiles
4. Count how many values are greater than 1
5. Count how many values are between -1 and 1

**Hint:** Use `np.random.normal()`, `np.percentile()`, `np.sum()` with boolean indexing

---

### Pandas Exercises

#### Exercise 6: Creating and Exploring DataFrames

Create a DataFrame with 50 records containing:
- Names (use a list of 10 names repeated)
- Ages (random between 20 and 60)
- Salaries (random between 30000 and 100000)
- Departments (Engineering, Sales, HR, Marketing)

Then:
1. Display the first and last 5 rows
2. Get basic statistics
3. Check data types
4. Count records per department

**Hint:** Use `pd.DataFrame()`, `df.head()`, `df.tail()`, `df.describe()`

#### Exercise 7: Data Selection and Filtering

Using the DataFrame from Exercise 6:
1. Select all names
2. Select age and salary columns
3. Get all rows where age > 30
4. Get all rows where salary > 50000
5. Get rows where age > 30 AND salary > 50000
6. Get rows where department is 'Engineering'

**Hint:** Use column selection, `df.loc[]`, `df.iloc[]`, and boolean indexing

#### Exercise 8: Adding and Modifying Columns

Using the DataFrame from Exercise 6:
1. Add a column for annual bonus (10% of salary)
2. Add a column for age group (young: <30, middle: 30-45, senior: >45)
3. Add a column for salary in thousands (salary/1000)
4. Update all salaries with a 5% raise
5. Create a column combining first name with department

**Hint:** Use direct assignment `df['col'] = ...` and `.apply()` with lambda functions

#### Exercise 9: Grouping and Aggregation

Using the DataFrame from Exercise 6:
1. Calculate average salary by department
2. Count employees per department
3. Get min and max salary per department
4. Calculate total bonus cost by department
5. Get all statistics (mean, sum, min, max, count) for salary by department

**Hint:** Use `df.groupby()`, `.agg()`, and multiple aggregation functions

#### Exercise 10: Sorting and Ranking

Using the DataFrame from Exercise 6:
1. Sort by salary (ascending and descending)
2. Sort by age (ascending)
3. Sort by department then by salary
4. Add a column ranking employees by salary within each department
5. Get the top 5 earners

**Hint:** Use `.sort_values()` and `.rank()`

---

### Data Manipulation and Cleaning

#### Exercise 11: Handling Missing Data

Create a DataFrame with some missing values:
```python
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, 8, 9],
    'C': [10, 20, 30, np.nan, 50]
})
```

For each approach, show what values remain:
1. Drop all rows with any missing values
2. Drop all rows where all values are missing
3. Fill missing values with 0
4. Fill missing values with column mean
5. Forward fill missing values

**Hint:** Use `.dropna()`, `.fillna()`, `.isnull()`

#### Exercise 12: Data Transformation

Create a DataFrame with sales data:
```python
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10),
    'product': ['A', 'B', 'A', 'B', 'C'] * 2,
    'sales': [100, 200, 150, 180, 220, 190, 210, 195, 230, 240]
})
```

1. Create new columns for year, month, and day from date
2. Create a column for sales category (low: <150, medium: 150-200, high: >200)
3. Normalize sales values (0-1 scale)
4. Create dummy variables for products
5. Calculate cumulative sales

**Hint:** Use `.dt` accessor, `.cut()`, `.get_dummies()`, `.cumsum()`

#### Exercise 13: Merging DataFrames

Create two DataFrames:
```python
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [1, 2, 1, 3]
})

departments = pd.DataFrame({
    'dept_id': [1, 2, 3],
    'dept_name': ['Engineering', 'Sales', 'HR']
})
```

1. Perform an inner join on dept_id
2. Perform a left join
3. Perform a right join
4. Concatenate the two DataFrames side by side
5. Concatenate them vertically

**Hint:** Use `.merge()`, `.concat()`, with different join types

#### Exercise 14: Pivot Tables

Using the DataFrame from Exercise 12:
1. Create a pivot table with products as rows and month as columns, with sales summed
2. Create a pivot table with mean sales by product
3. Use the pivot table to identify which product performs best each month

**Hint:** Use `.pivot_table()`

#### Exercise 15: Real-world Data Pipeline

Create a complete data pipeline:
1. Create a DataFrame with 100 customer records (name, age, purchase_amount, purchase_date, category)
2. Clean the data (handle missing values, duplicates)
3. Transform data (add new columns, create age groups)
4. Analyze (group by category, calculate metrics)
5. Identify top 10 customers by purchase amount
6. Calculate statistics per category

**Hint:** Chain multiple operations together

---

## Solutions Guide Structure

Each solution includes:
- Step-by-step code
- Expected output
- Explanation of approach
- Alternative approaches (if applicable)

See solutions.md for complete implementations.

---

## Tips for Success

1. **Test incrementally** - Run code after each step
2. **Use print statements** - Understand intermediate results
3. **Check data types** - Use `.info()` and `.dtype`
4. **Visualize results** - Use matplotlib to verify transformations
5. **Read error messages** - They usually explain what went wrong

---

## Challenge Progression

- Exercises 1-5: NumPy fundamentals
- Exercises 6-10: Pandas basics
- Exercises 11-15: Real-world data operations

Each exercise builds on previous knowledge. Complete them in order.
