# Essential Tools - Examples

## 20 Practical, Runnable Examples

### Example 1: Rich Console Basics

```python
# rich_basics.py
from rich.console import Console

console = Console()

# Basic printing
console.print("Hello, World!")

# Styled text
console.print("[bold red]Error:[/bold red] Something went wrong")
console.print("[green]Success:[/green] Operation completed")
console.print("[yellow]Warning:[/yellow] Check configuration")

# Multiple styles
console.print("[bold yellow on blue] IMPORTANT [/bold yellow on blue]")
console.print("[italic cyan]Loading...[/italic cyan]")
console.print("[underline]Underlined text[/underline]")

# Emojis
console.print(":rocket: Launching application")
console.print(":white_check_mark: All tests passed")
```

**Output:**
```
Hello, World!
Error: Something went wrong  (in red)
Success: Operation completed  (in green)
Warning: Check configuration  (in yellow)
 IMPORTANT   (yellow on blue background)
Loading...  (italic cyan)
Underlined text
🚀 Launching application
✓ All tests passed
```

---

### Example 2: Rich Tables

```python
# rich_tables.py
from rich.console import Console
from rich.table import Table

console = Console()

# Create table
table = Table(title="Student Grades", show_header=True, header_style="bold magenta")

# Add columns
table.add_column("Student", style="cyan", no_wrap=True)
table.add_column("Subject", style="white")
table.add_column("Grade", justify="right", style="green")
table.add_column("Status", justify="center")

# Add rows
table.add_row("Alice Johnson", "Mathematics", "95", "✓")
table.add_row("Bob Smith", "Physics", "88", "✓")
table.add_row("Charlie Brown", "Chemistry", "92", "✓")
table.add_row("Diana Prince", "Biology", "78", "○")

# Print table
console.print(table)

# Table with grid style
table2 = Table(title="Server Status", box=None)
table2.add_column("Server")
table2.add_column("Status")
table2.add_column("Uptime")

table2.add_row("web-01", "[green]Online[/green]", "45 days")
table2.add_row("db-01", "[green]Online[/green]", "32 days")
table2.add_row("cache-01", "[red]Offline[/red]", "0 days")

console.print(table2)
```

---

### Example 3: Rich Progress Bars

```python
# rich_progress.py
from rich.progress import track
from rich.console import Console
import time

console = Console()

# Simple progress bar
console.print("[bold]Processing files...[/bold]")
for i in track(range(100), description="Processing"):
    time.sleep(0.02)

# Multiple progress bars
from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Uploading...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.2)
        time.sleep(0.02)

console.print("[bold green]All tasks completed![/bold green]")
```

---

### Example 4: Rich Panels and Layout

```python
# rich_panels.py
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout

console = Console()

# Simple panels
console.print(Panel("Welcome to the application!", title="Greeting"))
console.print(Panel("[red]Critical error occurred![/red]", title="Error", border_style="red"))
console.print(Panel("[green]All systems operational[/green]", title="Status", border_style="green"))

# Layout with panels
layout = Layout()

layout.split_column(
    Layout(name="header"),
    Layout(name="main"),
    Layout(name="footer")
)

layout["header"].update(Panel("[bold blue]Application Dashboard[/bold blue]", style="blue"))
layout["main"].update(Panel("Main content area\nLine 2\nLine 3", title="Content"))
layout["footer"].update(Panel("© 2024 MyApp", style="dim"))

console.print(layout)

# Split layout
layout2 = Layout()
layout2.split_row(
    Layout(Panel("Left sidebar", style="cyan")),
    Layout(Panel("Main content", style="white")),
    Layout(Panel("Right sidebar", style="magenta"))
)

console.print(layout2)
```

---

### Example 5: Rich Syntax Highlighting

```python
# rich_syntax.py
from rich.console import Console
from rich.syntax import Syntax

console = Console()

# Python code highlighting
python_code = '''
def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
'''

syntax = Syntax(python_code, "python", theme="monokai", line_numbers=True)
console.print(syntax)

# JSON highlighting
json_code = '''
{
  "name": "Alice",
  "age": 30,
  "skills": ["Python", "JavaScript", "SQL"],
  "active": true
}
'''

syntax_json = Syntax(json_code, "json", theme="monokai", line_numbers=True)
console.print(syntax_json)

# SQL highlighting
sql_code = '''
SELECT users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE users.active = true
GROUP BY users.name
ORDER BY order_count DESC;
'''

syntax_sql = Syntax(sql_code, "sql", theme="monokai", line_numbers=True)
console.print(syntax_sql)
```

---

### Example 6: Click Basic CLI

```python
# click_basic.py
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='The person to greet')
def hello(count, name):
    """Simple greeting program"""
    for _ in range(count):
        click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    hello()
```

**Usage:**
```bash
$ python click_basic.py --count 3 --name Alice
Hello, Alice!
Hello, Alice!
Hello, Alice!

$ python click_basic.py
Your name: Bob
Hello, Bob!
```

---

### Example 7: Click with Multiple Commands

```python
# click_multi.py
import click

@click.group()
def cli():
    """A simple CLI tool with multiple commands"""
    pass

@cli.command()
@click.argument('name')
def greet(name):
    """Greet someone"""
    click.echo(f'Hello, {name}!')

@cli.command()
@click.argument('numbers', nargs=-1, type=int)
def sum(numbers):
    """Sum a list of numbers"""
    result = sum(numbers)
    click.echo(f'Sum: {result}')

@cli.command()
@click.option('--upper', is_flag=True, help='Convert to uppercase')
@click.argument('text')
def echo(upper, text):
    """Echo text"""
    if upper:
        text = text.upper()
    click.echo(text)

if __name__ == '__main__':
    cli()
```

**Usage:**
```bash
$ python click_multi.py greet Alice
Hello, Alice!

$ python click_multi.py sum 1 2 3 4 5
Sum: 15

$ python click_multi.py echo --upper "hello world"
HELLO WORLD
```

---

### Example 8: Click with File Operations

```python
# click_files.py
import click

@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@click.option('--upper', is_flag=True, help='Convert to uppercase')
def process(input, output, upper):
    """Process a file and write to output"""
    for line in input:
        if upper:
            line = line.upper()
        output.write(line)
    click.echo('File processed successfully')

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def count_lines(filename):
    """Count lines in a file"""
    with open(filename) as f:
        lines = len(f.readlines())
    click.echo(f'Lines: {lines}')

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def list_files(directory):
    """List files in directory"""
    import os
    files = os.listdir(directory)
    for file in files:
        click.echo(file)

if __name__ == '__main__':
    # Choose which command to run
    process()
```

---

### Example 9: Typer Simple CLI

```python
# typer_simple.py
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def hello(
    name: str,
    age: Optional[int] = None,
    formal: bool = False
):
    """Greet someone"""
    greeting = "Good day" if formal else "Hello"
    message = f"{greeting}, {name}!"
    if age:
        message += f" You are {age} years old."
    typer.echo(message)

@app.command()
def goodbye(name: str):
    """Say goodbye"""
    typer.echo(f"Goodbye, {name}!")

if __name__ == "__main__":
    app()
```

**Usage:**
```bash
$ python typer_simple.py hello Alice
Hello, Alice!

$ python typer_simple.py hello Alice --age 30
Hello, Alice! You are 30 years old.

$ python typer_simple.py hello Alice --formal
Good day, Alice!

$ python typer_simple.py goodbye Bob
Goodbye, Bob!
```

---

### Example 10: Typer with Enums and Choices

```python
# typer_enums.py
import typer
from enum import Enum

app = typer.Typer()

class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class Environment(str, Enum):
    DEV = "development"
    STAGING = "staging"
    PROD = "production"

@app.command()
def configure(
    log_level: LogLevel = LogLevel.INFO,
    environment: Environment = Environment.DEV,
    verbose: bool = False
):
    """Configure application settings"""
    typer.echo(f"Log Level: {log_level.value}")
    typer.echo(f"Environment: {environment.value}")
    typer.echo(f"Verbose: {verbose}")

@app.command()
def deploy(
    environment: Environment,
    confirm: bool = typer.Option(False, "--confirm", "-y")
):
    """Deploy application"""
    if not confirm:
        confirmed = typer.confirm(f"Deploy to {environment.value}?")
        if not confirmed:
            typer.echo("Deployment cancelled")
            raise typer.Abort()

    typer.echo(f"Deploying to {environment.value}...")
    typer.echo("Deployment successful!")

if __name__ == "__main__":
    app()
```

**Usage:**
```bash
$ python typer_enums.py configure --log-level debug --environment staging
Log Level: debug
Environment: staging
Verbose: False

$ python typer_enums.py deploy production
Deploy to production? [y/N]: y
Deploying to production...
Deployment successful!
```

---

### Example 11: Typer with Progress

```python
# typer_progress.py
import typer
import time

app = typer.Typer()

@app.command()
def download(files: int = 10):
    """Simulate downloading files"""
    with typer.progressbar(range(files), label="Downloading") as progress:
        for value in progress:
            time.sleep(0.1)
    typer.echo(f"Downloaded {files} files")

@app.command()
def process():
    """Process with custom progress"""
    items = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    with typer.progressbar(items, label="Processing files") as progress:
        for item in progress:
            typer.echo(f"\nProcessing {item}")
            time.sleep(0.5)

@app.command()
def backup():
    """Backup with status"""
    typer.echo("Starting backup...")

    tasks = [
        "Database",
        "User files",
        "Configuration",
        "Logs"
    ]

    for task in tasks:
        typer.echo(f"Backing up {task}...", nl=False)
        time.sleep(0.5)
        typer.echo(" [green]✓[/green]")

    typer.echo("Backup complete!")

if __name__ == "__main__":
    app()
```

---

### Example 12: Pydantic Basic Validation

```python
# pydantic_basic.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class User(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=20)
    email: str
    age: int = Field(ge=0, le=150)
    is_active: bool = True
    tags: List[str] = []

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v.lower()

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v.lower()

# Valid user
user1 = User(
    id=1,
    username="Alice123",
    email="Alice@Example.com",
    age=30
)
print(user1)
# Output: id=1 username='alice123' email='alice@example.com' age=30 is_active=True tags=[]

# Invalid user (raises ValidationError)
try:
    user2 = User(
        id=2,
        username="ab",  # Too short
        email="invalid",  # No @
        age=200  # Too old
    )
except Exception as e:
    print(f"Validation error: {e}")
```

---

### Example 13: Pydantic Advanced Features

```python
# pydantic_advanced.py
from pydantic import BaseModel, Field, computed_field, model_validator
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    discount: float = Field(ge=0, le=1, default=0)
    quantity: int = Field(ge=0, default=0)
    created_at: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def final_price(self) -> float:
        """Calculate price after discount"""
        return self.price * (1 - self.discount)

    @computed_field
    @property
    def total_value(self) -> float:
        """Calculate total inventory value"""
        return self.final_price * self.quantity

    @computed_field
    @property
    def in_stock(self) -> bool:
        """Check if product is in stock"""
        return self.quantity > 0

    @model_validator(mode='after')
    def validate_discount(self):
        if self.discount > 0.5:
            print(f"Warning: High discount of {self.discount*100}% on {self.name}")
        return self

# Create products
laptop = Product(
    name="Laptop",
    price=1000,
    discount=0.2,
    quantity=5
)

print(f"Product: {laptop.name}")
print(f"Price: ${laptop.price}")
print(f"Discount: {laptop.discount*100}%")
print(f"Final Price: ${laptop.final_price}")
print(f"Quantity: {laptop.quantity}")
print(f"Total Value: ${laptop.total_value}")
print(f"In Stock: {laptop.in_stock}")

# Serialize
print("\nJSON representation:")
print(laptop.model_dump_json(indent=2))
```

**Output:**
```
Product: Laptop
Price: $1000
Discount: 20.0%
Final Price: $800.0
Quantity: 5
Total Value: $4000.0
In Stock: True

JSON representation:
{
  "name": "Laptop",
  "price": 1000.0,
  "discount": 0.2,
  "quantity": 5,
  "created_at": "2024-01-29T10:30:00.123456"
}
```

---

### Example 14: Pydantic Settings Management

```python
# pydantic_settings.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Application settings
    app_name: str = "MyApp"
    debug: bool = False
    version: str = "1.0.0"

    # Database settings
    database_url: str = Field(default="sqlite:///./app.db")
    database_pool_size: int = 5

    # API settings
    api_key: str = Field(default="", description="API key for external service")
    api_timeout: int = 30

    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create .env file:
# APP_NAME=ProductionApp
# DEBUG=false
# DATABASE_URL=postgresql://localhost/mydb
# API_KEY=secret-key-123

# Load settings
settings = Settings()

print(f"App Name: {settings.app_name}")
print(f"Debug Mode: {settings.debug}")
print(f"Database: {settings.database_url}")
print(f"Server: {settings.host}:{settings.port}")

# Access settings
def get_database_connection():
    return settings.database_url

def is_debug_mode():
    return settings.debug
```

---

### Example 15: Loguru Basic Logging

```python
# loguru_basic.py
from loguru import logger
import sys

# Remove default handler
logger.remove()

# Add console handler with colors
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="DEBUG",
    colorize=True
)

# Add file handler
logger.add("app.log", rotation="10 MB", level="INFO")

# Log at different levels
logger.debug("Debug message - detailed information")
logger.info("Info message - general information")
logger.warning("Warning message - something unexpected")
logger.error("Error message - something went wrong")
logger.critical("Critical message - serious problem")

# Log with context
logger.info("User logged in", extra={"user_id": 123, "ip": "192.168.1.1"})

# Log exceptions
def divide(a, b):
    try:
        result = a / b
        logger.info(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        logger.exception("Division by zero error")
        return None

divide(10, 2)  # Success
divide(10, 0)  # Error with traceback
```

---

### Example 16: Loguru Advanced Features

```python
# loguru_advanced.py
from loguru import logger
import sys
import time

# Remove default handler
logger.remove()

# Development logging (colorized console)
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
    level="DEBUG",
    colorize=True
)

# Production logging (file with rotation)
logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="00:00",  # New file at midnight
    retention="30 days",  # Keep for 30 days
    compression="zip",  # Compress old files
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="INFO"
)

# Error-only log
logger.add(
    "logs/errors.log",
    rotation="50 MB",
    level="ERROR",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    backtrace=True,
    diagnose=True
)

# Structured logging with bind
request_logger = logger.bind(request_id="abc123", user_id=42)
request_logger.info("Processing request")
request_logger.info("Request completed")

# Catch decorator for automatic exception logging
@logger.catch
def risky_function():
    """Function that might fail"""
    return 1 / 0

# Use catch
try:
    risky_function()
except:
    pass  # Already logged by @logger.catch

# Timing operations
start = time.time()
logger.info("Starting long operation")
time.sleep(1)
duration = time.time() - start
logger.info(f"Operation completed in {duration:.2f}s")

# Conditional logging
DEBUG_MODE = True
if DEBUG_MODE:
    logger.debug("Debug information")
```

---

### Example 17: Loguru with Context and Filtering

```python
# loguru_context.py
from loguru import logger
import sys

# Remove default
logger.remove()

# Filter for specific modules
def module_filter(record):
    return record["extra"].get("module") == "payments"

# Payment-specific log
logger.add(
    "logs/payments.log",
    filter=module_filter,
    format="{time} | {level} | {message}",
    level="INFO"
)

# General log
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>",
    colorize=True
)

# Create specialized loggers
payment_logger = logger.bind(module="payments")
auth_logger = logger.bind(module="auth")
api_logger = logger.bind(module="api")

# Use specialized loggers
payment_logger.info("Payment processed", amount=100, user_id=123)
payment_logger.info("Refund issued", amount=50, user_id=123)

auth_logger.info("User login", user_id=123)
api_logger.info("API request", endpoint="/users", method="GET")

# These go to payments.log only
payment_logger.info("Payment gateway connected")

# Context manager for temporary context
with logger.contextualize(task="data_import"):
    logger.info("Starting import")
    logger.info("Importing 1000 records")
    logger.info("Import complete")
```

---

### Example 18: Complete CLI App with All Tools

```python
# task_manager.py
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from pydantic import BaseModel, Field
from loguru import logger
from typing import List, Optional
import sys
from datetime import datetime

# Setup
app = typer.Typer()
console = Console()

# Configure logging
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>",
    level="INFO",
    colorize=True
)
logger.add("task_manager.log", rotation="10 MB")

# Data model
class Task(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)

# In-memory storage
tasks: List[Task] = []
next_id = 1

@app.command()
def add(
    title: str,
    description: Optional[str] = None
):
    """Add a new task"""
    global next_id

    try:
        task = Task(id=next_id, title=title, description=description)
        tasks.append(task)
        next_id += 1

        logger.info(f"Task added: {title}")
        console.print(Panel(
            f"[green]✓[/green] Task added: {title}",
            title="Success",
            border_style="green"
        ))
    except Exception as e:
        logger.error(f"Failed to add task: {e}")
        console.print(f"[red]Error:[/red] {e}")

@app.command()
def list(show_completed: bool = False):
    """List all tasks"""
    if not tasks:
        console.print("[yellow]No tasks found[/yellow]")
        return

    # Filter tasks
    display_tasks = tasks if show_completed else [t for t in tasks if not t.completed]

    # Create table
    table = Table(title="Task List", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan", width=6)
    table.add_column("Title", style="white")
    table.add_column("Description", style="dim")
    table.add_column("Status", justify="center", width=10)

    for task in display_tasks:
        status = "[green]✓[/green]" if task.completed else "[yellow]○[/yellow]"
        table.add_row(
            str(task.id),
            task.title,
            task.description or "",
            status
        )

    console.print(table)
    logger.info(f"Listed {len(display_tasks)} tasks")

@app.command()
def complete(task_id: int):
    """Mark a task as completed"""
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            logger.info(f"Task completed: {task.title}")
            console.print(f"[green]✓[/green] Task {task_id} marked as completed")
            return

    console.print(f"[red]Error:[/red] Task {task_id} not found")
    logger.error(f"Task not found: {task_id}")

@app.command()
def delete(task_id: int):
    """Delete a task"""
    for i, task in enumerate(tasks):
        if task.id == task_id:
            if typer.confirm(f"Delete task '{task.title}'?"):
                deleted = tasks.pop(i)
                logger.info(f"Task deleted: {deleted.title}")
                console.print(f"[green]✓[/green] Task deleted")
            else:
                console.print("[yellow]Cancelled[/yellow]")
            return

    console.print(f"[red]Error:[/red] Task {task_id} not found")

@app.command()
def stats():
    """Show task statistics"""
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    pending = total - completed

    table = Table(title="Task Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="magenta")

    table.add_row("Total Tasks", str(total))
    table.add_row("Completed", str(completed))
    table.add_row("Pending", str(pending))

    if total > 0:
        completion_rate = (completed / total) * 100
        table.add_row("Completion Rate", f"{completion_rate:.1f}%")

    console.print(table)

if __name__ == "__main__":
    logger.info("Task Manager started")
    app()
```

**Usage:**
```bash
$ python task_manager.py add "Write documentation" --description "Complete API docs"
✓ Task added: Write documentation

$ python task_manager.py add "Review code"
✓ Task added: Review code

$ python task_manager.py list
┌────┬───────────────────┬─────────────────┬────────┐
│ ID │ Title             │ Description     │ Status │
├────┼───────────────────┼─────────────────┼────────┤
│ 1  │ Write documentation│ Complete API... │   ○    │
│ 2  │ Review code       │                 │   ○    │
└────┴───────────────────┴─────────────────┴────────┘

$ python task_manager.py complete 1
✓ Task 1 marked as completed

$ python task_manager.py stats
┌─────────────────┬───────┐
│ Metric          │ Value │
├─────────────────┼───────┤
│ Total Tasks     │     2 │
│ Completed       │     1 │
│ Pending         │     1 │
│ Completion Rate │ 50.0% │
└─────────────────┴───────┘
```

---

### Example 19: Rich Tree and Markdown

```python
# rich_tree_markdown.py
from rich.console import Console
from rich.tree import Tree
from rich.markdown import Markdown

console = Console()

# Tree structure
tree = Tree("[bold cyan]Project Structure[/bold cyan]")
src = tree.add("[yellow]src/[/yellow]")
src.add("[green]main.py[/green]")
src.add("[green]utils.py[/green]")
models = src.add("[yellow]models/[/yellow]")
models.add("[green]user.py[/green]")
models.add("[green]product.py[/green]")

tests = tree.add("[yellow]tests/[/yellow]")
tests.add("[green]test_main.py[/green]")
tests.add("[green]test_utils.py[/green]")

tree.add("[blue]README.md[/blue]")
tree.add("[blue]requirements.txt[/blue]")

console.print(tree)

# Markdown rendering
markdown_text = """
# Task Manager

## Features

- Add tasks
- List tasks
- Complete tasks
- Delete tasks

## Installation

```bash
pip install typer rich pydantic loguru
```

## Usage

```python
python task_manager.py add "My task"
python task_manager.py list
```

**Note**: This is a demo application.
"""

md = Markdown(markdown_text)
console.print(md)
```

---

### Example 20: Production-Ready Application Template

```python
# production_app.py
import typer
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field
from loguru import logger
import sys
from pathlib import Path
from typing import Optional

# Settings
class Settings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    log_level: str = "INFO"
    log_file: str = "app.log"

    class Config:
        env_file = ".env"

settings = Settings()

# Setup logging
logger.remove()

if settings.debug:
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{module}</cyan> - <level>{message}</level>",
        level=settings.log_level,
        colorize=True
    )

logger.add(
    settings.log_file,
    rotation="10 MB",
    retention="30 days",
    compression="gz",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {module}:{function}:{line} - {message}",
    level=settings.log_level
)

# Models
class DataRecord(BaseModel):
    id: int
    name: str = Field(min_length=1)
    value: float = Field(ge=0)

# App
app = typer.Typer()
console = Console()

@app.command()
def process(
    input_file: Path = typer.Argument(..., exists=True),
    output_file: Optional[Path] = None,
    verbose: bool = False
):
    """Process data file"""
    logger.info(f"Processing file: {input_file}")

    if verbose:
        console.print(f"[cyan]Input:[/cyan] {input_file}")
        if output_file:
            console.print(f"[cyan]Output:[/cyan] {output_file}")

    # Simulate processing
    records = []
    with Progress() as progress:
        task = progress.add_task("Processing...", total=100)

        for i in range(100):
            # Simulate work
            record = DataRecord(id=i, name=f"Item {i}", value=float(i * 10))
            records.append(record)
            progress.update(task, advance=1)

    logger.info(f"Processed {len(records)} records")

    # Display results
    table = Table(title="Processing Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Records Processed", str(len(records)))
    table.add_row("Input File", str(input_file))
    if output_file:
        table.add_row("Output File", str(output_file))

    console.print(table)

@app.command()
def info():
    """Show application information"""
    console.print(f"[bold]{settings.app_name}[/bold]")
    console.print(f"Debug Mode: {settings.debug}")
    console.print(f"Log Level: {settings.log_level}")
    console.print(f"Log File: {settings.log_file}")

@logger.catch
def main():
    """Main entry point with error catching"""
    logger.info(f"{settings.app_name} started")
    app()

if __name__ == "__main__":
    main()
```

---

## Summary

These 20 examples demonstrate:

1. **Rich (Examples 1-5, 19)**: Console output, tables, progress bars, panels, syntax highlighting, trees, markdown
2. **Click (Examples 6-8)**: Basic CLI, multiple commands, file operations
3. **Typer (Examples 9-11)**: Simple CLI, enums, progress bars
4. **Pydantic (Examples 12-14)**: Validation, advanced features, settings management
5. **Loguru (Examples 15-17)**: Basic logging, advanced features, context and filtering
6. **Combined (Examples 18, 20)**: Real-world applications using all tools together

All examples are complete, runnable, and demonstrate best practices for each tool.
