# Developer Tools - Exercises

## 15 Progressive Challenges

### Black Formatting Exercises

#### Exercise 1: Format Messy Code

Given messy Python code:
1. Apply Black formatting
2. Observe changes
3. Document what Black changed

**Messy Code Example:**
```python
def calculate(x,y,z):
    result=x+y*z
    return result
data=[1,2,3,4,5]
for item in data:
    print('Item:',item)
```

**Tasks:**
- Run Black on the file
- Compare before and after
- List all formatting changes made

#### Exercise 2: Black Configuration

1. Create pyproject.toml with Black settings
2. Configure line length
3. Configure target Python version
4. Test with sample code

---

### Ruff Linting Exercises

#### Exercise 3: Identify and Fix Issues

Create Python file with intentional Ruff violations:
1. Unused imports
2. Unused variables
3. Multiple statements on one line
4. Missing newline at EOF

Run Ruff and fix all issues.

#### Exercise 4: Ruff Configuration

1. Create ruff configuration in pyproject.toml
2. Select specific rules
3. Ignore certain rules
4. Create per-file overrides
5. Test configuration

**Requirements:**
- Select E and F rules
- Ignore E501 (line length)
- Allow F401 in __init__.py files

---

### pytest Testing Exercises

#### Exercise 5: Write Simple Unit Tests

Create test file for calculator functions:
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Write tests covering:
- Normal cases
- Edge cases
- Error conditions

#### Exercise 6: Use Fixtures

Create fixtures for:
1. Sample data setup
2. Temporary file creation
3. Database setup (mock)
4. API client setup (mock)

Write tests using these fixtures.

#### Exercise 7: Parametrized Tests

Create parametrized tests for:
1. Email validation
2. Password strength validation
3. Number formatting

Test multiple cases with one test function.

#### Exercise 8: Test Organization

Organize tests as:
1. Unit tests directory
2. Integration tests directory
3. Fixtures in conftest.py
4. Run tests and verify organization

---

### Poetry Dependency Management

#### Exercise 9: Create Project with Poetry

1. Create new project with `poetry new`
2. Add dependencies (requests, flask, sqlalchemy)
3. Add dev dependencies (pytest, black, ruff, mypy)
4. Create pyproject.toml with proper metadata
5. Install dependencies

**Requirements:**
- Project name: mylearningapp
- Python version: ^3.9
- At least 5 regular dependencies
- At least 5 dev dependencies

#### Exercise 10: Dependency Constraints

1. Create pyproject.toml with various version constraints
2. Use caret (^), tilde (~), and range operators
3. Document why each constraint is used
4. Test with poetry update

**Examples:**
- ^2.0 (compatible versions)
- ~2.0 (patch releases)
- >=2.0,<3.0 (version range)

---

### mypy Type Checking

#### Exercise 11: Add Type Hints

Add type hints to:
1. Function parameters
2. Function return types
3. Variable annotations
4. Collection types (List, Dict, etc)

Example functions:
```python
def greet(name):
    return f"Hello, {name}"

def sum_list(numbers):
    return sum(numbers)

def get_user_by_id(user_id):
    return {'id': user_id, 'name': 'John'}
```

#### Exercise 12: Type Checking Configuration

1. Create mypy configuration
2. Enable strict options
3. Add type ignore comments where needed
4. Verify all code type checks

---

### Pre-commit Hooks

#### Exercise 13: Set Up Pre-commit

1. Create .pre-commit-config.yaml
2. Include: Black, Ruff, mypy, pytest
3. Install hooks with `pre-commit install`
4. Test by committing code

**Configuration:**
- Black hook for formatting
- Ruff hook with --fix
- mypy hook for type checking
- Local pytest hook

#### Exercise 14: Git Workflow with Hooks

1. Create sample code with issues
2. Attempt to commit
3. Observe hooks failing
4. Fix issues
5. Successfully commit

**Steps:**
- Create code file with violations
- Stage file: `git add`
- Commit: `git commit`
- Fix issues when hooks fail
- Retry commit

---

### Complete Project Setup

#### Exercise 15: Full Development Workflow

Create complete project with:
1. Poetry initialization
2. Black formatting
3. Ruff linting
4. mypy type checking
5. pytest testing
6. Pre-commit hooks

**Project Structure:**
```
myproject/
├── pyproject.toml
├── .pre-commit-config.yaml
├── README.md
├── src/myproject/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   └── test_calculator.py
└── .gitignore
```

**Requirements:**
- All files properly formatted
- No linting issues
- All type hints complete
- Tests passing (>80% coverage)
- Hooks configured and working

---

## Advanced Challenges

### Challenge A: CI/CD Pipeline

Create GitHub Actions workflow:
- Run Black check
- Run Ruff check
- Run mypy check
- Run pytest
- Generate coverage report

### Challenge B: Custom Pre-commit Hook

Write custom pre-commit hook that:
- Checks for hardcoded passwords
- Validates commit message format
- Ensures docstrings present

### Challenge C: Performance Profiling

Profile code to find:
- Slow functions
- Memory leaks
- Inefficient algorithms

### Challenge D: Documentation Generation

Generate project documentation using:
- Sphinx or pdoc
- Include docstrings
- Auto-generate API docs

---

## Hints and Tips

1. **Start Simple**: Get one tool working before combining
2. **Test Frequently**: Run tests after each change
3. **Read Error Messages**: They guide you to solutions
4. **Version Control**: Commit before major changes
5. **Iterate**: Tool configuration improves over time
6. **Automate**: Let hooks and CI do the work
7. **Document**: Keep configuration documented

---

## Challenge Progression

1. **Exercises 1-4**: Black and Ruff basics
2. **Exercises 5-8**: pytest fundamentals
3. **Exercises 9-10**: Poetry dependency management
4. **Exercises 11-12**: mypy type checking
5. **Exercises 13-14**: Pre-commit hooks
6. **Exercise 15**: Complete integration
7. **Advanced**: Real-world scenarios

Complete exercises in order for best understanding.
