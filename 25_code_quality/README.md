# Chapter 25: Code Quality Tools

## Overview

This chapter covers essential code quality tools for Python: Black (formatting), Ruff (linting), mypy (type checking), and pre-commit hooks (automation). You'll learn how to maintain professional code quality automatically.

## What You'll Learn

- **Black**: Automatic code formatting for consistency
- **Ruff**: Lightning-fast linting for code quality  
- **mypy**: Static type checking for safer code
- **pre-commit**: Automated quality checks before commits
- **CI/CD Integration**: Automating quality in pipelines

## Why It Matters

Code quality tools ensure:
- Consistent, readable code across teams
- Early detection of bugs and issues
- Maintainable, well-documented code
- Automated quality enforcement
- Professional development standards

## Prerequisites

- Python fundamentals (Chapters 1-7)
- Chapter 23: Testing with pytest
- Chapter 24: Package Management
- Basic Git knowledge
- Command-line skills

## Installation

```bash
# Install with pip
pip install black ruff mypy pre-commit

# Or with Poetry
poetry add --group dev black ruff mypy pre-commit
```

## Quick Start

### Format with Black

```bash
black myfile.py  # Format file
black .          # Format project
```

### Lint with Ruff

```bash
ruff check .          # Check for issues
ruff check --fix .    # Fix auto-fixable issues
```

### Type Check with mypy

```bash
mypy myfile.py   # Check file
mypy .           # Check project
```

### Setup Pre-commit

```bash
pre-commit install              # Install hooks
pre-commit run --all-files      # Run on all files
```

## Key Takeaways

By the end of this chapter, you'll be able to:
1. Format code automatically with Black
2. Identify and fix code quality issues with Ruff
3. Add type hints and use mypy for type checking
4. Automate code checks with pre-commit hooks
5. Integrate quality tools into CI/CD pipelines
6. Build professional development workflows

---

**Time to Complete**: 4-6 hours
**Difficulty**: Intermediate
**Practice Projects**: 3-5 project setups recommended
