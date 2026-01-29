# Chapter 8: File I/O and Path Handling

## Learning Objectives

- Read and write files
- Use pathlib for path operations
- Work with CSV, JSON, XML
- Handle binary files
- Use context managers

## Quick Reference

```python
# Text file
with open('file.txt') as f:
    content = f.read()

# pathlib (modern)
from pathlib import Path
path = Path('data/file.txt')
content = path.read_text()

# JSON
import json
data = json.load(open('data.json'))

# CSV
import csv
with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

## Prerequisites

- Chapters 1-7

## Estimated Time

- 2-3 hours

## Next Chapter

**Chapter 9: Itertools and Functional Tools**
