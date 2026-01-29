# Code Quality Tools - Tips

## Black Tips

### Integrate with Editor
```bash
# VS Code: "python.formatting.provider": "black"
```

### Configuration
```toml
[tool.black]
line-length = 88
```

## Ruff Tips

### Fix Imports Automatically
```bash
ruff check --fix .
```

### Understand Error Codes
```
F401: imported but unused
E501: line too long
W292: no newline at end
```

## mypy Tips

### Type Hints Best Practices
```python
from typing import Optional, List, Dict

def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
```

### Ignore Errors Selectively
```python
result = some_function()  # type: ignore
```

## pre-commit Tips

### Run Hooks Manually
```bash
pre-commit run --all-files
pre-commit run black --all-files
```

### Skip Hooks
```bash
git commit --no-verify  # Skip all hooks
```

## Integration Workflow

```bash
# 1. Format
black .

# 2. Lint
ruff check --fix .

# 3. Type check
mypy .

# 4. Test
pytest

# 5. Commit (hooks verify)
git commit -m "message"
```

For complete tips, see original 25_dev_tools/tips.md.
