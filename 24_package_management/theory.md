# Package Management - Theory

## Table of Contents

1. [Introduction to Package Management](#introduction-to-package-management)
2. [pip Basics](#pip-basics)
3. [Virtual Environments](#virtual-environments)
4. [Poetry Introduction](#poetry-introduction)
5. [Project Structure](#project-structure)
6. [pyproject.toml](#pyprojecttoml)
7. [Version Constraints](#version-constraints)
8. [Poetry Commands](#poetry-commands)
9. [Lock Files](#lock-files)
10. [Publishing Packages](#publishing-packages)

---

## Introduction to Package Management

### What is Package Management?

Package management handles:
- Installing external libraries
- Managing dependencies
- Resolving version conflicts
- Creating reproducible environments
- Distributing your own packages

### Why Use Package Managers?

```
Without Package Manager:
  ├─ Manual dependency tracking
  ├─ Version conflicts
  ├─ Difficult collaboration
  └─ Hard to reproduce environments

With Package Manager (Poetry):
  ├─ Automatic dependency resolution
  ├─ Version conflict detection
  ├─ Easy team collaboration
  └─ Reproducible environments
```

---

## pip Basics

### What is pip?

pip is Python's package installer:
- Installs packages from PyPI (Python Package Index)
- Basic dependency management
- Comes with Python 3.4+

### Basic pip Commands

```bash
# Install package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install from requirements.txt
pip install -r requirements.txt

# Uninstall package
pip uninstall requests

# List installed packages
pip list

# Show package info
pip show requests

# Freeze dependencies
pip freeze > requirements.txt
```

### requirements.txt

```txt
# requirements.txt
requests==2.28.0
flask>=2.0.0,<3.0.0
numpy~=1.23.0
pandas
```

---

## Virtual Environments

### Why Virtual Environments?

Virtual environments provide:
- Isolated Python environments
- Project-specific dependencies
- No global pollution
- Different Python versions per project

### Creating Virtual Environments

#### Using venv (Built-in)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install packages
pip install requests

# Deactivate
deactivate
```

#### Using virtualenv

```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

## Poetry Introduction

### What is Poetry?

Poetry is a modern Python packaging and dependency management tool that provides:
- Dependency version management
- Virtual environment management automatically
- Package publishing capabilities
- Lock files for reproducible builds
- Dependency conflict resolution
- Simple, clean pyproject.toml configuration

### Poetry Advantages

```
pip + venv:
  ├─ Manual venv creation
  ├─ requirements.txt management
  ├─ No lock file
  └─ Manual conflict resolution

Poetry:
  ├─ Automatic venv management
  ├─ pyproject.toml configuration
  ├─ poetry.lock for reproducibility
  └─ Automatic conflict resolution
```

### Installation

```bash
# Install Poetry (recommended method)
curl -sSL https://install.python-poetry.org | python3 -

# Or with pip (not recommended)
pip install poetry

# Verify
poetry --version

# Update Poetry
poetry self update
```

---

## Project Structure

### Creating Project with Poetry

```bash
# Create new project
poetry new myproject

# Generated structure:
myproject/
├── pyproject.toml       # Project configuration
├── README.md
├── myproject/           # Source code
│   └── __init__.py
└── tests/               # Tests
    └── __init__.py
```

### Initializing Existing Project

```bash
# Initialize Poetry in existing project
cd existing_project
poetry init

# Follow interactive prompts:
# - Package name
# - Version
# - Description
# - Author
# - License
# - Dependencies
```

---

## pyproject.toml

### Basic Configuration

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My awesome project"
authors = ["John Doe <john@example.com>"]
readme = "README.md"
license = "MIT"
homepage = "https://github.com/user/myproject"
repository = "https://github.com/user/myproject"
keywords = ["example", "project"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.0"
fastapi = "^0.95.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
black = "^23.1"
ruff = "^0.1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Dependency Groups

```toml
[tool.poetry.dependencies]
# Production dependencies
python = "^3.9"
requests = "^2.28"

[tool.poetry.group.dev.dependencies]
# Development dependencies
pytest = "^7.2"
black = "^23.1"

[tool.poetry.group.docs.dependencies]
# Documentation dependencies
sphinx = "^5.0"

[tool.poetry.group.test.dependencies]
# Test-specific dependencies
pytest-cov = "^4.0"
```

### Scripts

```toml
[tool.poetry.scripts]
# Define command-line scripts
myapp = "myproject.main:main"
cli = "myproject.cli:run"

# Now you can run:
# poetry run myapp
# poetry run cli
```

---

## Version Constraints

### Semantic Versioning

```
Version Format: MAJOR.MINOR.PATCH
Example: 2.28.1

MAJOR: Breaking changes
MINOR: New features (backward compatible)
PATCH: Bug fixes
```

### Constraint Operators

```toml
# Exact version
requests = "2.28.0"

# Caret (^) - Compatible version (recommended)
requests = "^2.28.0"    # >=2.28.0, <3.0.0

# Tilde (~) - Approximate version
requests = "~2.28.0"    # >=2.28.0, <2.29.0

# Comparison operators
requests = ">=2.28.0"   # Greater than or equal
requests = "<=2.28.0"   # Less than or equal
requests = ">2.0,<3.0"  # Range

# Wildcard
requests = "2.*"        # Any 2.x version

# Multiple constraints
requests = ">=2.28,!=2.28.2,<3.0"

# Any version (avoid in production)
requests = "*"
```

### Version Constraint Examples

```toml
[tool.poetry.dependencies]
python = "^3.9"                    # >= 3.9, < 4.0
requests = "^2.28"                 # >= 2.28, < 3.0
flask = "~2.3"                     # >= 2.3, < 2.4
sqlalchemy = ">=1.4,<2.0"          # Specific range
python-dotenv = "^0.19"            # >= 0.19, < 1.0
pydantic = ">=1.7,!=1.8.0,<2.0"   # Range with exclusion
```

---

## Poetry Commands

### Dependency Management

```bash
# Add dependency
poetry add requests
poetry add fastapi uvicorn

# Add dev dependency
poetry add --group dev pytest black ruff

# Add specific version
poetry add "requests==2.28.0"
poetry add "requests^2.28"

# Remove dependency
poetry remove requests

# Install all dependencies
poetry install

# Install without dev dependencies
poetry install --no-dev

# Install specific group
poetry install --with docs

# Update dependencies
poetry update

# Update specific package
poetry update requests

# Show what would update (dry run)
poetry update --dry-run
```

### Environment Management

```bash
# Show virtual environment info
poetry env info

# List virtual environments
poetry env list

# Use specific Python version
poetry env use python3.9
poetry env use 3.10

# Remove virtual environment
poetry env remove python3.9

# Run command in environment
poetry run python script.py
poetry run pytest

# Activate shell (subshell)
poetry shell

# Exit shell
exit
```

### Package Information

```bash
# Show installed packages
poetry show

# Show package details
poetry show requests

# Show dependency tree
poetry show --tree

# Show outdated packages
poetry show --outdated

# Check pyproject.toml validity
poetry check
```

### Building and Publishing

```bash
# Build package (creates dist/)
poetry build

# Publish to PyPI
poetry config pypi-token.pypi YOUR_TOKEN
poetry publish

# Build and publish
poetry publish --build

# Publish to private repository
poetry config repositories.internal https://repo.example.com
poetry publish --repository internal
```

---

## Lock Files

### What is poetry.lock?

poetry.lock contains:
- Exact versions of all dependencies
- Transitive dependencies
- Hashes for security
- Ensures reproducible installs

### Lock File Workflow

```
Developer A:
1. poetry add requests
2. poetry.lock updated
3. Commit poetry.lock to Git

Developer B:
1. git pull
2. poetry install
3. Gets exact same versions
```

### Lock File Commands

```bash
# Generate/update lock file
poetry lock

# Update without installing
poetry lock --no-update

# Install from lock file
poetry install

# Show what's locked
poetry show --tree
```

### Best Practices

```bash
# DO commit poetry.lock
git add poetry.lock
git commit -m "Update dependencies"

# DON'T manually edit poetry.lock
# Let Poetry manage it

# DO keep it updated
poetry update  # When you want to update
```

---

## Publishing Packages

### Preparing for Publishing

```toml
# pyproject.toml
[tool.poetry]
name = "mypackage"
version = "0.1.0"
description = "A useful package"
authors = ["Your Name <you@example.com>"]
readme = "README.md"
license = "MIT"
keywords = ["example", "package"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

[tool.poetry.dependencies]
python = "^3.9"
```

### Building Package

```bash
# Build package
poetry build

# Creates:
# dist/
# ├── mypackage-0.1.0-py3-none-any.whl
# └── mypackage-0.1.0.tar.gz
```

### Publishing to PyPI

```bash
# Configure PyPI token
poetry config pypi-token.pypi pypi-YOUR_TOKEN_HERE

# Publish
poetry publish

# Or build and publish together
poetry publish --build
```

### Publishing to Test PyPI

```bash
# Configure test PyPI
poetry config repositories.testpypi https://test.pypi.org/legacy/

# Get token from test.pypi.org
poetry config pypi-token.testpypi pypi-YOUR_TEST_TOKEN_HERE

# Publish to test PyPI
poetry publish --repository testpypi
```

---

## Best Practices

### Dependency Management

1. **Use Poetry for new projects**
2. **Always commit poetry.lock**
3. **Use version constraints wisely**
4. **Separate dev dependencies**
5. **Update regularly but carefully**

### Version Constraints

```toml
# GOOD: Allows patches and minors
requests = "^2.28.0"

# GOOD: Very restrictive (libraries)
requests = "~2.28.0"

# OKAY: For internal tools
requests = ">=2.28.0"

# BAD: No constraint (avoid)
requests = "*"
```

### Project Organization

```
myproject/
├── pyproject.toml       # Poetry config
├── poetry.lock          # Locked dependencies
├── README.md            # Documentation
├── src/                 # Source code
│   └── myproject/
│       ├── __init__.py
│       └── main.py
├── tests/               # Tests
│   └── test_main.py
└── .gitignore           # Git ignore
```

---

## Summary

### Key Concepts

1. **Virtual Environments**: Isolated Python environments
2. **Poetry**: Modern dependency management
3. **pyproject.toml**: Project configuration
4. **Version Constraints**: Control dependency versions
5. **Lock Files**: Reproducible installs
6. **Publishing**: Share packages with others

### Poetry Workflow

```
1. poetry new myproject   # Create project
2. poetry add requests    # Add dependencies
3. poetry install         # Install dependencies
4. poetry run pytest      # Run in environment
5. poetry update          # Update dependencies
6. git commit            # Commit lock file
```

### Command Quick Reference

```bash
poetry new project        # Create project
poetry init              # Initialize existing
poetry add package       # Add dependency
poetry install           # Install dependencies
poetry update            # Update dependencies
poetry run command       # Run in environment
poetry shell             # Activate shell
poetry build             # Build package
poetry publish           # Publish to PyPI
```

---

## Next Steps

After mastering Poetry:
1. Learn Chapter 25: Code Quality Tools
2. Explore packaging best practices
3. Study continuous integration
4. Learn about private package repositories
5. Understand dependency security
