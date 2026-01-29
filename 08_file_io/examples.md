# File I/O and Path Handling: Code Examples

## Example 1: Basic File Reading

```python
# Read entire file
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

# Read lines as list
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# Read line by line (memory efficient)
with open('data.txt') as f:
    for line in f:
        print(line.strip())

# Read specific number of lines
with open('data.txt') as f:
    first_line = f.readline()
    second_line = f.readline()
```

## Example 2: Basic File Writing

```python
# Write file (overwrites)
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Second line\n')

# Write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)

# Append to file
with open('output.txt', 'a') as f:
    f.write('Appended line\n')

# Write with print
with open('output.txt', 'w') as f:
    print('Hello', 'World', file=f)
    print('Another line', file=f)
```

## Example 3: pathlib - Modern Path Operations

```python
from pathlib import Path

# Create path object
path = Path('data/files/document.txt')

# Path properties
print(path.name)       # 'document.txt'
print(path.stem)       # 'document'
print(path.suffix)     # '.txt'
print(path.parent)     # Path('data/files')
print(path.parts)      # ('data', 'files', 'document.txt')

# Check existence
print(path.exists())
print(path.is_file())
print(path.is_dir())

# Read and write
content = path.read_text()  # Read as string
data = path.read_bytes()    # Read as bytes

path.write_text('Hello, World!')
path.write_bytes(b'Binary data')

# Create directories
path.parent.mkdir(parents=True, exist_ok=True)

# Join paths
base = Path('data')
file_path = base / 'subfolder' / 'file.txt'
```

## Example 4: Working with Directories

```python
from pathlib import Path

# List files in directory
data_dir = Path('data')

# All files
for file in data_dir.iterdir():
    print(file)

# Filter by extension
for txt_file in data_dir.glob('*.txt'):
    print(txt_file)

# Recursive search
for py_file in data_dir.rglob('*.py'):
    print(py_file)

# Create directory structure
new_dir = Path('output/results/2024')
new_dir.mkdir(parents=True, exist_ok=True)

# Remove directory
import shutil
shutil.rmtree('old_directory')
```

## Example 5: CSV Files

```python
import csv
from pathlib import Path

# Write CSV
data = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

with open('people.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Read CSV
with open('people.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['age']} years old, lives in {row['city']}")

# CSV with list of lists
with open('matrix.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['A', 'B', 'C'])
    writer.writerow([1, 2, 3])
    writer.writerow([4, 5, 6])
```

## Example 6: JSON Files

```python
import json
from pathlib import Path

# Write JSON
data = {
    'users': [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ],
    'count': 2,
    'timestamp': '2024-01-01'
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Or using pathlib
Path('data.json').write_text(json.dumps(data, indent=2))

# Read JSON
with open('data.json') as f:
    loaded_data = json.load(f)

# Or using pathlib
loaded_data = json.loads(Path('data.json').read_text())

# Pretty print JSON
print(json.dumps(data, indent=2))

# Compact JSON (no whitespace)
compact = json.dumps(data, separators=(',', ':'))
```

## Example 7: Binary Files

```python
from pathlib import Path

# Copy binary file
source = Path('image.png')
dest = Path('copy.png')

data = source.read_bytes()
dest.write_bytes(data)

# Or with open()
with open('image.png', 'rb') as f_in:
    with open('copy.png', 'wb') as f_out:
        f_out.write(f_in.read())

# Read binary in chunks (for large files)
with open('large_file.bin', 'rb') as f:
    while True:
        chunk = f.read(1024)  # Read 1KB at a time
        if not chunk:
            break
        process(chunk)
```

## Example 8: Temporary Files

```python
import tempfile
from pathlib import Path

# Temporary file (auto-deleted)
with tempfile.TemporaryFile(mode='w+') as f:
    f.write('Temporary data')
    f.seek(0)
    print(f.read())
# File is deleted here

# Named temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('Data to keep temporarily')
    temp_path = f.name

print(f"Temp file: {temp_path}")
# Delete manually later
Path(temp_path).unlink()

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    temp_path = Path(tmpdir)
    (temp_path / 'file.txt').write_text('Temp file')
    # Do work in tmpdir
# Directory and contents deleted here
```

## Example 9: File Metadata

```python
from pathlib import Path
import os
from datetime import datetime

path = Path('data.txt')

# File size
size_bytes = path.stat().st_size
size_kb = size_bytes / 1024
print(f"Size: {size_kb:.2f} KB")

# Modification time
mtime = path.stat().st_mtime
mod_time = datetime.fromtimestamp(mtime)
print(f"Modified: {mod_time}")

# Permissions
mode = path.stat().st_mode
print(f"Permissions: {oct(mode)}")

# Using os module
print(f"Size: {os.path.getsize('data.txt')} bytes")
print(f"Modified: {os.path.getmtime('data.txt')}")
```

## Example 10: File Operations

```python
from pathlib import Path
import shutil

# Copy file
shutil.copy('source.txt', 'dest.txt')
shutil.copy2('source.txt', 'dest.txt')  # Preserves metadata

# Move/rename file
shutil.move('old_name.txt', 'new_name.txt')
Path('old.txt').rename('new.txt')  # pathlib way

# Delete file
Path('unwanted.txt').unlink()  # Doesn't fail if missing
Path('unwanted.txt').unlink(missing_ok=True)

# Copy directory tree
shutil.copytree('source_dir', 'dest_dir')

# Remove directory tree
shutil.rmtree('directory_to_remove')
```

## Example 11: Context Manager for Multiple Files

```python
# Read from one file, write to another
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.upper())

# Multiple files
with open('file1.txt') as f1, \
     open('file2.txt') as f2, \
     open('output.txt', 'w') as out:
    out.write(f1.read())
    out.write(f2.read())
```

## Example 12: Error Handling

```python
from pathlib import Path

def safe_read_file(filename):
    """Safely read file with error handling."""
    try:
        path = Path(filename)
        return path.read_text()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except PermissionError:
        print(f"Permission denied: {filename}")
        return None
    except UnicodeDecodeError:
        print(f"Not a text file: {filename}")
        # Try binary
        return path.read_bytes()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

# Usage
content = safe_read_file('data.txt')
if content:
    process(content)
```

## Example 13: Processing Large Files

```python
def process_large_file(filename):
    """Process large file line by line."""
    line_count = 0
    total_length = 0

    with open(filename) as f:
        for line in f:
            line_count += 1
            total_length += len(line)

            # Process line
            if 'ERROR' in line:
                print(f"Line {line_count}: {line.strip()}")

    avg_length = total_length / line_count if line_count > 0 else 0
    print(f"Processed {line_count} lines, avg length: {avg_length:.1f}")
```

## Example 14: Configuration Files (INI)

```python
import configparser

# Write config
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes'
}
config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'user': 'admin'
}

with open('config.ini', 'w') as f:
    config.write(f)

# Read config
config = configparser.ConfigParser()
config.read('config.ini')

print(config['database']['host'])  # 'localhost'
print(config.getint('DEFAULT', 'ServerAliveInterval'))  # 45
print(config.getboolean('DEFAULT', 'Compression'))  # True
```

## Example 15: Line-by-Line File Comparison

```python
def compare_files(file1, file2):
    """Compare two files line by line."""
    with open(file1) as f1, open(file2) as f2:
        for i, (line1, line2) in enumerate(zip(f1, f2), start=1):
            if line1 != line2:
                print(f"Difference at line {i}:")
                print(f"  File 1: {line1.rstrip()}")
                print(f"  File 2: {line2.rstrip()}")

compare_files('version1.txt', 'version2.txt')
```

See solutions.md for exercise answers!
