# Essential Tools - Theory

## Table of Contents

1. [Introduction](#introduction)
2. [Rich - Terminal Formatting](#rich-terminal-formatting)
3. [Click - CLI Framework](#click-cli-framework)
4. [Typer - Modern CLI](#typer-modern-cli)
5. [Pydantic - Data Validation](#pydantic-data-validation)
6. [Loguru - Advanced Logging](#loguru-advanced-logging)
7. [Combining Tools](#combining-tools)
8. [Best Practices](#best-practices)

---

## Introduction

### Why These Tools?

Essential Python tools solve common development problems:

```
Rich      → Beautiful terminal output
Click     → Powerful CLI framework
Typer     → Type-hinted CLI (built on Click)
Pydantic  → Data validation and settings
Loguru    → Simple, powerful logging
```

### When to Use Each Tool

| Tool | Use Case | Alternative |
|------|----------|------------|
| Rich | Terminal UI, progress bars | print(), tqdm |
| Click | Complex CLI apps | argparse |
| Typer | Simple CLI with types | Click, argparse |
| Pydantic | Data validation, API models | dataclasses |
| Loguru | Application logging | logging module |

---

## Rich - Terminal Formatting

### What is Rich?

Rich is a Python library for rich text and beautiful formatting in the terminal. It provides a simple API for colors, tables, progress bars, syntax highlighting, and more.

### Core Components

#### 1. Console

The main interface for Rich output:

```python
from rich.console import Console

console = Console()

# Basic printing
console.print("Hello, World!")

# Styled text
console.print("[bold red]Error![/bold red]")
console.print("[green]Success[/green]")

# Multiple styles
console.print("[bold yellow on blue]Warning[/bold yellow on blue]")
```

#### 2. Text Styles

Rich supports various text styles:

```
Bold:       [bold]text[/bold]
Italic:     [italic]text[/italic]
Underline:  [underline]text[/underline]
Strike:     [strike]text[/strike]
Colors:     [red]text[/red]
Background: [on blue]text[/on blue]
Combined:   [bold red on yellow]text[/bold red on yellow]
```

#### 3. Tables

Create formatted tables:

```python
from rich.table import Table

table = Table(title="Student Grades")
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Subject", style="magenta")
table.add_column("Grade", justify="right", style="green")

table.add_row("Alice", "Math", "95")
table.add_row("Bob", "Science", "88")
table.add_row("Charlie", "English", "92")

console.print(table)
```

#### 4. Progress Bars

Track long-running operations:

```python
from rich.progress import track
import time

for i in track(range(100), description="Processing..."):
    time.sleep(0.01)
```

#### 5. Panels

Create bordered panels:

```python
from rich.panel import Panel

console.print(Panel("Hello, World!", title="Greeting"))
console.print(Panel("[red]Error occurred[/red]", title="Error", border_style="red"))
```

#### 6. Syntax Highlighting

Display code with syntax highlighting:

```python
from rich.syntax import Syntax

code = '''
def hello(name):
    print(f"Hello, {name}!")
'''

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

#### 7. Layout

Create complex layouts:

```python
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()
layout.split_column(
    Layout(Panel("Header", style="bold blue")),
    Layout(Panel("Body content")),
    Layout(Panel("Footer", style="bold green"))
)

console.print(layout)
```

### Rich Features Summary

| Feature | Purpose | Method |
|---------|---------|--------|
| Console | Basic output | `console.print()` |
| Styling | Colored text | `[red]text[/red]` |
| Tables | Tabular data | `Table()` |
| Progress | Long operations | `track()`, `Progress()` |
| Panels | Bordered boxes | `Panel()` |
| Syntax | Code highlighting | `Syntax()` |
| Layout | Complex UI | `Layout()` |
| Markdown | Render markdown | `Markdown()` |

---

## Click - CLI Framework

### What is Click?

Click is a Python package for creating command-line interfaces with minimal code. It's designed to make writing CLI tools quick and fun.

### Core Concepts

#### 1. Commands

Basic command definition:

```python
import click

@click.command()
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()
```

#### 2. Options

Add command-line options:

```python
@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='The person to greet')
def hello(count, name):
    for _ in range(count):
        click.echo(f'Hello, {name}!')
```

#### 3. Arguments

Positional arguments:

```python
@click.command()
@click.argument('filename')
def cat(filename):
    with open(filename) as f:
        click.echo(f.read())
```

#### 4. Types

Click supports various parameter types:

```python
@click.command()
@click.option('--count', type=int)
@click.option('--ratio', type=float)
@click.option('--flag', is_flag=True)
@click.option('--choice', type=click.Choice(['A', 'B', 'C']))
@click.option('--path', type=click.Path(exists=True))
def process(count, ratio, flag, choice, path):
    pass
```

#### 5. Groups

Create command groups:

```python
@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo('Initialized')

@cli.command()
def run():
    click.echo('Running')

# Usage: python app.py init
#        python app.py run
```

#### 6. Context

Share data between commands:

```python
@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = True

@cli.command()
@click.pass_context
def status(ctx):
    if ctx.obj['verbose']:
        click.echo('Verbose mode enabled')
```

---

## Typer - Modern CLI

### What is Typer?

Typer is a modern CLI framework built on Click that uses Python type hints for parameter validation and help text generation.

### Why Typer?

```python
# Click (more code)
@click.command()
@click.option('--name', type=str, help='Your name')
@click.option('--age', type=int, help='Your age')
def hello(name: str, age: int):
    pass

# Typer (less code, same result)
def hello(name: str, age: int):
    pass
```

### Core Features

#### 1. Simple Commands

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()
```

#### 2. Type Hints as Validation

```python
from typing import Optional

@app.command()
def greet(
    name: str,                    # Required argument
    age: int = 0,                 # Optional with default
    formal: bool = False,         # Boolean flag
    title: Optional[str] = None   # Optional argument
):
    greeting = f"{'Mr./Ms.' if formal else 'Hey'} {name}"
    if age:
        greeting += f", age {age}"
    typer.echo(greeting)
```

#### 3. Enums for Choices

```python
from enum import Enum

class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

@app.command()
def log(level: LogLevel):
    typer.echo(f"Logging at level: {level.value}")
```

#### 4. File Parameters

```python
from pathlib import Path

@app.command()
def read_file(
    file: typer.FileText,
    output: typer.FileTextWrite = typer.Option(None)
):
    content = file.read()
    if output:
        output.write(content)
    else:
        typer.echo(content)
```

#### 5. Progress Bars

```python
import time

@app.command()
def process():
    with typer.progressbar(range(100)) as progress:
        for value in progress:
            time.sleep(0.01)
```

#### 6. Confirmation

```python
@app.command()
def delete():
    if typer.confirm("Are you sure?"):
        typer.echo("Deleting...")
    else:
        typer.echo("Cancelled")
```

### Typer vs Click

| Feature | Click | Typer |
|---------|-------|-------|
| Syntax | Decorators | Type hints |
| Learning curve | Steeper | Gentler |
| Boilerplate | More | Less |
| Type checking | Manual | Automatic |
| Best for | Complex CLIs | Simple CLIs |

---

## Pydantic - Data Validation

### What is Pydantic?

Pydantic provides data validation using Python type annotations. It's the most widely used data validation library for Python.

### Core Concepts

#### 1. BaseModel

The foundation of Pydantic:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

# Create instance (automatic validation)
user = User(id=1, name="Alice", email="alice@example.com", age=30)
print(user.name)  # Alice
print(user.model_dump())  # {'id': 1, 'name': 'Alice', ...}
```

#### 2. Type Validation

Pydantic validates types automatically:

```python
from typing import List, Dict, Optional

class Product(BaseModel):
    name: str
    price: float
    tags: List[str]
    metadata: Dict[str, str]
    description: Optional[str] = None

# This works
product = Product(
    name="Laptop",
    price=999.99,
    tags=["electronics", "computers"],
    metadata={"brand": "Dell"}
)

# This raises ValidationError
# product = Product(name="Laptop", price="invalid", tags=[], metadata={})
```

#### 3. Field Validation

Add constraints to fields:

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    age: int = Field(ge=0, le=150)  # ge = greater or equal
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    score: float = Field(gt=0, lt=100)  # gt = greater than
```

#### 4. Custom Validators

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v.lower()

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.title()
```

#### 5. Model Validators

Validate entire model:

```python
from pydantic import BaseModel, model_validator

class DateRange(BaseModel):
    start_date: str
    end_date: str

    @model_validator(mode='after')
    def check_dates(self):
        if self.start_date > self.end_date:
            raise ValueError('start_date must be before end_date')
        return self
```

#### 6. Computed Fields

```python
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height
```

#### 7. Settings Management

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

# Automatically loads from environment variables or .env file
settings = Settings()
```

#### 8. JSON Serialization

```python
class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=30)

# To dict
data = user.model_dump()

# To JSON
json_str = user.model_dump_json()

# From dict
user2 = User.model_validate({"name": "Bob", "age": 25})

# From JSON
user3 = User.model_validate_json('{"name": "Charlie", "age": 35}')
```

### Pydantic Features

| Feature | Purpose | Method |
|---------|---------|--------|
| BaseModel | Base class | Inherit from it |
| Field | Add constraints | `Field()` |
| Validators | Custom validation | `@field_validator` |
| Model validators | Validate entire model | `@model_validator` |
| Computed fields | Derived values | `@computed_field` |
| Settings | Config management | `BaseSettings` |
| Serialization | JSON/dict conversion | `model_dump()` |

---

## Loguru - Advanced Logging

### What is Loguru?

Loguru is a library that aims to make logging in Python enjoyable. It provides a simple API with powerful features out of the box.

### Why Loguru?

Standard logging is complex:

```python
import logging

# Standard logging (verbose)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

Loguru is simple:

```python
from loguru import logger

# Loguru (simple)
logger.add("app.log", rotation="500 MB")
```

### Core Features

#### 1. Basic Logging

```python
from loguru import logger

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

#### 2. File Rotation

Automatically rotate log files:

```python
# Rotate when file reaches 500 MB
logger.add("app.log", rotation="500 MB")

# Rotate daily at midnight
logger.add("app.log", rotation="00:00")

# Rotate weekly
logger.add("app.log", rotation="1 week")

# Keep only 10 files
logger.add("app.log", rotation="500 MB", retention=10)
```

#### 3. Log Formatting

Customize log format:

```python
logger.add(
    "app.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO"
)

# With colors (terminal only)
logger.add(
    sys.stderr,
    format="<green>{time}</green> <level>{message}</level>",
    colorize=True
)
```

#### 4. Structured Logging

Add context to logs:

```python
logger.bind(user="alice").info("User logged in")
logger.bind(request_id="123").error("Request failed")

# Output: 2024-01-29 ... | user=alice | User logged in
```

#### 5. Exception Logging

Automatic traceback capture:

```python
@logger.catch
def risky_function():
    return 1 / 0

# Automatically logs full traceback
risky_function()
```

#### 6. Log Levels

```python
# Set minimum level
logger.add("app.log", level="WARNING")  # Only WARNING and above

# Filter by function
def my_filter(record):
    return record["extra"].get("special")

logger.add("special.log", filter=my_filter)
logger.bind(special=True).info("This will be logged")
```

#### 7. Serialization

Log as JSON:

```python
logger.add("api.log", serialize=True)

# Output: {"text": "...", "record": {"time": "...", "level": "INFO", ...}}
```

#### 8. Compression

Compress old logs:

```python
logger.add(
    "app.log",
    rotation="500 MB",
    compression="zip"  # or "gz", "bz2", "xz"
)
```

### Loguru Configuration Patterns

#### Development Setup

```python
from loguru import logger
import sys

# Remove default handler
logger.remove()

# Add colorized console output
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="DEBUG",
    colorize=True
)
```

#### Production Setup

```python
from loguru import logger

# Remove default handler
logger.remove()

# File logging with rotation
logger.add(
    "logs/app.log",
    rotation="100 MB",
    retention="30 days",
    compression="gz",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="INFO"
)

# Error-only log
logger.add(
    "logs/errors.log",
    rotation="50 MB",
    retention="90 days",
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    backtrace=True,
    diagnose=True
)
```

---

## Combining Tools

### Example: CLI Application

Combining all tools in one application:

```python
# app.py
import typer
from rich.console import Console
from rich.table import Table
from pydantic import BaseModel, Field
from loguru import logger

# Setup
app = typer.Typer()
console = Console()
logger.add("app.log", rotation="10 MB")

# Data model
class Task(BaseModel):
    id: int
    title: str = Field(min_length=1)
    completed: bool = False

# In-memory storage
tasks = []

@app.command()
def add(title: str):
    """Add a new task"""
    task = Task(id=len(tasks) + 1, title=title)
    tasks.append(task)
    logger.info(f"Task added: {title}")
    console.print(f"[green]✓[/green] Added: {title}")

@app.command()
def list():
    """List all tasks"""
    if not tasks:
        console.print("[yellow]No tasks found[/yellow]")
        return

    table = Table(title="Tasks")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="white")
    table.add_column("Status", style="green")

    for task in tasks:
        status = "✓" if task.completed else "○"
        table.add_row(str(task.id), task.title, status)

    console.print(table)
    logger.info(f"Listed {len(tasks)} tasks")

if __name__ == "__main__":
    app()
```

Usage:
```bash
python app.py add "Write documentation"
python app.py add "Review code"
python app.py list
```

---

## Best Practices

### 1. Rich Best Practices

```python
# Use Console consistently
console = Console()

# Use context managers for live updates
with console.status("Processing..."):
    # Long operation
    pass

# Use Progress for loops
from rich.progress import Progress

with Progress() as progress:
    task = progress.add_task("Processing", total=100)
    for i in range(100):
        progress.update(task, advance=1)
```

### 2. Click/Typer Best Practices

```python
# Validate early
@app.command()
def process(count: int = typer.Option(..., min=1, max=100)):
    pass

# Use groups for organization
@app.command()
def db():
    """Database commands"""
    pass

@db.command()
def migrate():
    """Run migrations"""
    pass
```

### 3. Pydantic Best Practices

```python
# Use Field for documentation
class User(BaseModel):
    name: str = Field(..., description="User's full name", min_length=2)
    age: int = Field(..., description="User's age", ge=0, le=150)

# Use aliases for external APIs
class APIUser(BaseModel):
    user_name: str = Field(alias="userName")
    user_email: str = Field(alias="userEmail")

    class Config:
        populate_by_name = True
```

### 4. Loguru Best Practices

```python
# Use catch decorator for critical functions
@logger.catch
def main():
    pass

# Add context with bind
logger = logger.bind(request_id=request_id)

# Use structured logging
logger.info("User action", user=user_id, action="login")

# Configure once at startup
def setup_logging(debug: bool = False):
    logger.remove()
    logger.add(
        sys.stderr,
        level="DEBUG" if debug else "INFO",
        colorize=True
    )
    logger.add(
        "app.log",
        rotation="10 MB",
        level="INFO"
    )
```

---

## Summary

### Quick Reference

| Tool | Key Class | Primary Use | One-liner |
|------|-----------|-------------|-----------|
| Rich | Console | Terminal UI | `console.print("[green]OK[/green]")` |
| Click | @click.command | CLI framework | `@click.command()` |
| Typer | Typer() | Type-hinted CLI | `app = typer.Typer()` |
| Pydantic | BaseModel | Data validation | `class User(BaseModel): ...` |
| Loguru | logger | Logging | `logger.info("message")` |

### When to Use What

```
Terminal output? → Rich
CLI application? → Typer (simple) or Click (complex)
Data validation? → Pydantic
Logging? → Loguru
All together? → Powerful professional app!
```

### Installation Summary

```bash
pip install rich click typer pydantic loguru pydantic-settings
```

---

## Next Steps

After mastering these essential tools:
1. Build a complete CLI application combining all tools
2. Explore Rich's advanced features (Live, Layout, Tree)
3. Study Pydantic's advanced validation patterns
4. Learn about logging aggregation (ELK, Splunk)
5. Integrate these tools into larger projects
