# File I/O: Tips

## Tip 1: Always Use Context Managers

**Bad**:
```python
f = open('file.txt')
content = f.read()
f.close()  # Might not execute if error!
```

**Good**:
```python
with open('file.txt') as f:
    content = f.read()
# Automatically closed
```

## Tip 2: Use pathlib

**Old way**:
```python
import os
path = os.path.join('data', 'file.txt')
if os.path.exists(path):
    with open(path) as f:
        content = f.read()
```

**Modern way**:
```python
from pathlib import Path
path = Path('data') / 'file.txt'
if path.exists():
    content = path.read_text()
```

## Tip 3: Handle Errors

```python
from pathlib import Path

try:
    content = Path('file.txt').read_text()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

## Gotcha: Line Endings

Different OS have different line endings:
- Unix: `\n`
- Windows: `\r\n`
- Mac (old): `\r`

Python handles this automatically in text mode!

See examples.md!
