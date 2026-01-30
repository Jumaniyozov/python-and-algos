# Chapter 25: Developer Tools

## Overview

This chapter covers essential developer tools and workflows for professional Python development. You'll learn code formatting, linting, testing, dependency management, and pre-commit hooks that keep code quality high and development workflows efficient.

## What You'll Learn

- **Black**: Automatic code formatting for consistency
- **Ruff**: Lightning-fast linter for code quality
- **pytest**: Comprehensive testing framework
- **Poetry**: Modern dependency and project management
- **mypy**: Static type checking for safer code
- **pre-commit**: Automated hooks for code quality
- **Development Workflows**: Professional development practices

## Why It Matters

Developer tools ensure:
- Consistent, readable code across teams
- Early detection of bugs and issues
- Maintainable, well-documented code
- Reproducible development environments
- Automated quality checks
- Professional project structure

## Prerequisites

- Python fundamentals (Chapters 1-7)
- Project structure understanding
- Basic command-line skills
- Git basics (for pre-commit hooks)

## Installation

```bash
# Install developer tools
pip install black ruff pytest mypy poetry pre-commit

# Or install as development dependencies
poetry add --group dev black ruff pytest mypy pre-commit
```

## Chapter Structure

1. **Theory** (`theory.md`): Core concepts and tools
2. **Examples** (`examples.md`): 15 practical, runnable examples
3. **Exercises** (`exercises.md`): 15 progressive challenges
4. **Solutions** (`solutions.md`): Detailed solutions
5. **Tips** (`tips.md`): Best practices and workflows

## Quick Start

### Format Code with Black

```bash
# Format a file
black myfile.py

# Format entire project
black .

# Check without modifying
black --check .
```

### Lint with Ruff

```bash
# Check code
ruff check .

# Fix auto-fixable issues
ruff check --fix .
```

### Run Tests with pytest

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_module.py

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

### Manage Dependencies with Poetry

```bash
# Create new project
poetry new myproject

# Add dependency
poetry add requests

# Add dev dependency
poetry add --group dev pytest

# Install dependencies
poetry install

# Run command in virtual environment
poetry run python script.py
```

### Type Check with mypy

```bash
# Check entire project
mypy .

# Check specific file
mypy myfile.py

# Ignore missing imports
mypy --ignore-missing-imports .
```

### Set Up Pre-commit Hooks

```bash
# Initialize pre-commit
pre-commit install

# Run on all files
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

## Real-World Applications

- Professional Python projects
- Open source contributions
- Team collaboration and code reviews
- CI/CD pipelines
- Code quality maintenance
- Bug prevention and detection
- Performance optimization

## Key Takeaways

By the end of this chapter, you'll be able to:
1. Format code automatically with Black
2. Identify code quality issues with Ruff
3. Write and run comprehensive tests
4. Manage project dependencies with Poetry
5. Use static type checking with mypy
6. Automate code checks with pre-commit hooks
7. Build professional development workflows

## Next Steps

After mastering this chapter:
- Set up CI/CD pipelines (GitHub Actions, GitLab CI)
- Learn performance profiling and optimization
- Explore code coverage tools (coverage.py)
- Master debugging techniques (pdb, debuggers)
- Study documentation generation (Sphinx)

---

**Time to Complete**: 8-10 hours
**Difficulty**: Intermediate to Advanced
**Practice Projects**: 3-5 complete project setups recommended
