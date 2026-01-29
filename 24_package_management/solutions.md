# Package Management - Solutions

## Solution 1: Create Project

```bash
poetry new mylearningapp
cd mylearningapp
poetry add requests flask sqlalchemy python-dotenv pydantic
poetry add --group dev pytest pytest-cov black ruff mypy pre-commit
```

## Solution 2: Version Constraints

```toml
[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28"
flask = "~2.3"
sqlalchemy = ">=1.4,<2.0"
```

For complete solutions, see solutions.md from original 25_dev_tools (solutions 9-10).
