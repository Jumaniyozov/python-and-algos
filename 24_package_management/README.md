# Chapter 24: Package Management with Poetry

## Overview

This chapter covers Python package and dependency management using Poetry, the modern solution for Python project management. You'll learn virtual environments, dependency resolution, version constraints, and publishing packages.

## What You'll Learn

- **pip Basics**: Traditional package installation
- **Virtual Environments**: Isolated Python environments (venv, virtualenv)
- **Poetry**: Modern dependency and project management
- **pyproject.toml**: Project configuration standard
- **Version Constraints**: Semantic versioning and dependency ranges
- **Lock Files**: Reproducible builds with poetry.lock
- **Publishing**: Packaging and publishing to PyPI

## Why It Matters

Package management ensures:
- Reproducible development environments
- No dependency conflicts
- Easy collaboration across teams
- Simple deployment processes
- Version control for dependencies
- Professional project structure

## Prerequisites

- Python fundamentals (Chapters 1-7)
- Command-line basics
- Understanding of modules and imports
- Basic Git knowledge (helpful)

## Installation

```bash
# Install Poetry (recommended)
curl -sSL https://install.python-poetry.org | python3 -

# Or with pip
pip install poetry

# Verify installation
poetry --version
```

## Quick Start

### Create New Project

```bash
# Create project with Poetry
poetry new myproject
cd myproject

# Project structure created:
# myproject/
# ├── pyproject.toml
# ├── README.md
# ├── myproject/
# │   └── __init__.py
# └── tests/
#     └── __init__.py
```

### Manage Dependencies

```bash
# Add dependency
poetry add requests

# Add dev dependency
poetry add --group dev pytest

# Install all dependencies
poetry install

# Update dependencies
poetry update
```

### Run Commands

```bash
# Run Python in Poetry environment
poetry run python script.py

# Run tests
poetry run pytest

# Activate shell
poetry shell
```

## Key Takeaways

By the end of this chapter, you'll be able to:
1. Create and manage virtual environments
2. Use Poetry for dependency management
3. Configure projects with pyproject.toml
4. Understand version constraints
5. Work with lock files for reproducibility
6. Publish packages to PyPI
7. Collaborate effectively on Python projects

---

**Time to Complete**: 3-5 hours
**Difficulty**: Beginner to Intermediate
**Practice Projects**: 3-5 project setups recommended
