# File I/O and Path Handling: Exercise Solutions

## Solution 1: Word Counter

```python
from pathlib import Path
from collections import Counter

def count_words(filename):
    """Count words in a file."""
    try:
        content = Path(filename).read_text()
        words = content.lower().split()
        return dict(Counter(words))
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return {}
    except Exception as e:
        print(f"Error: {e}")
        return {}

# Test
counts = count_words('sample.txt')
print(counts)
```

## Solution 2: CSV Processor

```python
import csv

def process_scores(input_file, output_file):
    """Add grades to scores CSV."""
    with open(input_file) as f_in:
        reader = csv.DictReader(f_in)
        rows = list(reader)

    # Calculate average
    scores = [int(row['score']) for row in rows]
    average = sum(scores) / len(scores)
    print(f"Average score: {average:.2f}")

    # Add grades
    def get_grade(score):
        score = int(score)
        if score >= 90: return 'A'
        if score >= 80: return 'B'
        if score >= 70: return 'C'
        if score >= 60: return 'D'
        return 'F'

    for row in rows:
        row['grade'] = get_grade(row['score'])

    # Write output
    with open(output_file, 'w', newline='') as f_out:
        fieldnames = ['name', 'score', 'grade']
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Test
process_scores('scores.csv', 'scores_with_grades.csv')
```

## Solution 3: JSON Configuration Manager

```python
import json
from pathlib import Path

class ConfigManager:
    """Manage JSON configuration."""

    def __init__(self, config_file, defaults=None):
        self.config_file = Path(config_file)
        self.defaults = defaults or {}
        self.config = self._load()

    def _load(self):
        """Load config from file or create default."""
        if self.config_file.exists():
            return json.loads(self.config_file.read_text())
        else:
            self.save()
            return self.defaults.copy()

    def get(self, key, default=None):
        """Get config value."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Set config value."""
        self.config[key] = value

    def save(self):
        """Save config to file."""
        self.config_file.write_text(json.dumps(self.config, indent=2))

# Test
config = ConfigManager('app_config.json', {'theme': 'dark', 'lang': 'en'})
print(config.get('theme'))  # 'dark'
config.set('theme', 'light')
config.save()
```

## Solution 4: File Backup

```python
from pathlib import Path
from datetime import datetime
import shutil

def backup_file(filename):
    """Create timestamped backup of file."""
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"{filename} not found")

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_name = f"{path.name}.{timestamp}.bak"
    backup_path = path.parent / backup_name

    shutil.copy2(path, backup_path)
    return str(backup_path)

# Test
backup = backup_file('important.txt')
print(f"Backup created: {backup}")
```

## Solution 5: Directory Tree

```python
from pathlib import Path

def print_tree(path, indent=0):
    """Print directory tree recursively."""
    path = Path(path)

    if path.is_file():
        print('  ' * indent + path.name)
    elif path.is_dir():
        print('  ' * indent + path.name + '/')
        for item in sorted(path.iterdir()):
            print_tree(item, indent + 1)

# Test
print_tree('data')
```

## Solution 6: Log File Analyzer

```python
from collections import defaultdict

def analyze_log(log_file):
    """Analyze log file and count message types."""
    stats = defaultdict(int)
    total_lines = 0

    with open(log_file) as f:
        for line in f:
            total_lines += 1
            line = line.strip()

            if 'ERROR' in line:
                stats['ERROR'] += 1
            elif 'WARNING' in line:
                stats['WARNING'] += 1
            elif 'INFO' in line:
                stats['INFO'] += 1

    stats['TOTAL'] = total_lines
    return dict(stats)

# Test
stats = analyze_log('app.log')
print(stats)
# {'ERROR': 5, 'WARNING': 12, 'INFO': 100, 'TOTAL': 117}
```

## Solution 7: File Merger

```python
from pathlib import Path

def merge_files(file_list, output_file):
    """Merge multiple files into one."""
    with open(output_file, 'w') as out:
        for filename in file_list:
            # Write header
            out.write(f"\n{'='*60}\n")
            out.write(f"File: {filename}\n")
            out.write(f"{'='*60}\n\n")

            # Write content
            content = Path(filename).read_text()
            out.write(content)
            out.write('\n')

    print(f"Merged {len(file_list)} files into {output_file}")

# Test
merge_files(['file1.txt', 'file2.txt', 'file3.txt'], 'merged.txt')
```

## Solution 8: Path Utilities

```python
from pathlib import Path

def get_file_extension(path):
    """Get file extension."""
    return Path(path).suffix

def change_extension(path, new_ext):
    """Change file extension."""
    path = Path(path)
    if not new_ext.startswith('.'):
        new_ext = '.' + new_ext
    return path.with_suffix(new_ext)

def get_filename_without_ext(path):
    """Get filename without extension."""
    return Path(path).stem

# Test
print(get_file_extension('document.txt'))  # '.txt'
print(change_extension('file.txt', '.md'))  # 'file.md'
print(get_filename_without_ext('report.pdf'))  # 'report'
```

## Solution 9: Binary File Splitter

```python
from pathlib import Path

def split_file(filename, chunk_size=1024*1024):
    """Split file into chunks."""
    path = Path(filename)
    chunks = []
    part_num = 1

    with open(path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            part_name = f"{path.name}.part{part_num}"
            part_path = path.parent / part_name

            part_path.write_bytes(chunk)
            chunks.append(str(part_path))
            part_num += 1

    return chunks

# Test
parts = split_file('large_file.bin', chunk_size=1024*1024)  # 1MB chunks
print(f"Split into {len(parts)} parts")
```

## Solution 10: CSV to JSON Converter

```python
import csv
import json
from pathlib import Path

def csv_to_json(csv_file, json_file):
    """Convert CSV to JSON."""
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        data = list(reader)

    Path(json_file).write_text(json.dumps(data, indent=2))
    print(f"Converted {len(data)} rows to JSON")

# With nested structures
def csv_to_json_nested(csv_file, json_file):
    """Convert CSV to JSON with nested structure support."""
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        rows = []

        for row in reader:
            nested = {}
            for key, value in row.items():
                if '.' in key:
                    # Handle nested keys like "address.city"
                    parts = key.split('.')
                    current = nested
                    for part in parts[:-1]:
                        if part not in current:
                            current[part] = {}
                        current = current[part]
                    current[parts[-1]] = value
                else:
                    nested[key] = value
            rows.append(nested)

    Path(json_file).write_text(json.dumps(rows, indent=2))

# Test
csv_to_json('data.csv', 'data.json')
```

## Challenge 1: File Watcher

```python
import time
import threading
from pathlib import Path

class FileWatcher:
    """Monitor file for changes."""

    def __init__(self, filename, callback, interval=1):
        self.path = Path(filename)
        self.callback = callback
        self.interval = interval
        self.running = False
        self.thread = None
        self.last_modified = None

    def start(self):
        """Start watching file."""
        self.running = True
        self.last_modified = self.path.stat().st_mtime if self.path.exists() else None
        self.thread = threading.Thread(target=self._watch)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        """Stop watching file."""
        self.running = False
        if self.thread:
            self.thread.join()

    def _watch(self):
        """Watch loop."""
        while self.running:
            if self.path.exists():
                current_mtime = self.path.stat().st_mtime
                if current_mtime != self.last_modified:
                    self.callback(str(self.path))
                    self.last_modified = current_mtime
            time.sleep(self.interval)

# Test
def on_change(filename):
    print(f"{filename} was modified!")

watcher = FileWatcher('watched_file.txt', on_change)
watcher.start()
# ... do other work ...
# watcher.stop()
```

## Challenge 2: Smart File Differ

```python
def diff_files(file1, file2):
    """Show differences between two files."""
    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else None
        line2 = lines2[i] if i < len(lines2) else None

        if line1 == line2:
            print(f"  {i+1}: {line1.rstrip()}")
        elif line1 is None:
            print(f"+ {i+1}: {line2.rstrip()}")
        elif line2 is None:
            print(f"- {i+1}: {line1.rstrip()}")
        else:
            print(f"- {i+1}: {line1.rstrip()}")
            print(f"+ {i+1}: {line2.rstrip()}")

# Test
diff_files('version1.txt', 'version2.txt')
```

## Challenge 3: Atomic File Writer

```python
import tempfile
from pathlib import Path
import shutil

def atomic_write(filename, content):
    """Write file atomically to prevent data loss."""
    path = Path(filename)

    # Write to temporary file in same directory
    with tempfile.NamedTemporaryFile(
        mode='w',
        dir=path.parent,
        delete=False,
        suffix='.tmp'
    ) as tmp_file:
        tmp_path = Path(tmp_file.name)
        tmp_file.write(content)

    try:
        # Atomic rename (replaces original)
        tmp_path.replace(path)
        return True
    except Exception as e:
        # Clean up temp file on error
        tmp_path.unlink(missing_ok=True)
        raise

# Test
try:
    atomic_write('important.txt', 'Critical data')
    print("Write successful")
except Exception as e:
    print(f"Write failed: {e}")
```

Excellent work! Check examples.md for more patterns.
