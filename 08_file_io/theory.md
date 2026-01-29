# File I/O: Theory

## 8.1 Reading and Writing Files

### Basic File Operations

```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read lines
with open('file.txt') as f:
    lines = f.readlines()  # List of lines

# Read line by line (memory efficient)
with open('file.txt') as f:
    for line in f:
        print(line.strip())

# Write file
with open('output.txt', 'w') as f:
    f.write('Hello\n')
    f.write('World\n')

# Append
with open('file.txt', 'a') as f:
    f.write('New line\n')
```

### File Modes
- `'r'` - Read (default)
- `'w'` - Write (overwrites)
- `'a'` - Append
- `'x'` - Exclusive creation
- `'b'` - Binary mode
- `'t'` - Text mode (default)
- `'+'` - Read and write

## 8.2 pathlib Module

```python
from pathlib import Path

# Create path
path = Path('data/file.txt')

# Properties
path.name  # 'file.txt'
path.stem  # 'file'
path.suffix  # '.txt'
path.parent  # Path('data')
path.exists()  # True/False

# Operations
path.read_text()  # Read file
path.write_text('content')  # Write file
path.mkdir(parents=True, exist_ok=True)  # Create directory

# Globbing
for p in Path('.').glob('*.py'):
    print(p)
```

## 8.3 Working with CSV, JSON

### CSV

```python
import csv

# Read CSV
with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# Write CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30})
```

### JSON

```python
import json

# Read JSON
with open('data.json') as f:
    data = json.load(f)

# Write JSON
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# String conversion
json_str = json.dumps({'key': 'value'})
data = json.loads(json_str)
```

## 8.4 Binary Files

```python
# Read binary
with open('image.png', 'rb') as f:
    data = f.read()

# Write binary
with open('copy.png', 'wb') as f:
    f.write(data)
```

## 8.5 tempfile

```python
import tempfile

# Temporary file
with tempfile.TemporaryFile(mode='w+') as f:
    f.write('temporary data')
    f.seek(0)
    print(f.read())

# Named temporary file
with tempfile.NamedTemporaryFile(delete=False) as f:
    f.write(b'data')
    temp_name = f.name
```

## Best Practices

- Always use context managers (`with`)
- Use pathlib for path operations
- Handle file not found errors
- Close files properly

See examples.md!
