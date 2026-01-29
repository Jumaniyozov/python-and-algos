# Package Management - Tips

## Poetry Tips

### 1. Virtual Environment Management

```bash
poetry run python script.py
poetry run pytest
poetry shell  # Activate shell
```

### 2. Lock File Management

```bash
# Lock file (poetry.lock) should be committed
poetry update  # Update all dependencies
poetry update requests  # Update specific package
```

### 3. Development Groups

```toml
[tool.poetry.group.dev.dependencies]
pytest = "^7.0"

[tool.poetry.group.docs.dependencies]
sphinx = "^5.0"
```

### 4. Publishing Packages

```bash
poetry build
poetry config pypi-token.pypi YOUR_TOKEN
poetry publish
```

## Command Reference

```bash
poetry new project        # Create project
poetry add package       # Add dependency
poetry install           # Install dependencies
poetry update            # Update dependencies
poetry run command       # Run in environment
poetry show              # List dependencies
poetry build             # Build package
poetry publish           # Publish to PyPI
```

For complete tips, see tips.md from original 25_dev_tools (Poetry sections).
