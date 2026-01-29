# Essential Tools - Tips and Best Practices

## Rich Tips

### 1. Console Best Practices

```python
# ✓ Good: Create console once and reuse
console = Console()
console.print("Message 1")
console.print("Message 2")

# ✗ Bad: Creating new console each time
Console().print("Message 1")
Console().print("Message 2")
```

### 2. Use Context Managers

```python
# For live updates
with console.status("Processing..."):
    do_work()

# For progress bars
with Progress() as progress:
    task = progress.add_task("Working", total=100)
    for i in range(100):
        progress.update(task, advance=1)
```

### 3. Error Highlighting

```python
# Use colors for different message types
console.print("[green]Success[/green]")
console.print("[yellow]Warning[/yellow]")
console.print("[red]Error[/red]")
console.print("[dim]Debug info[/dim]")
```

### 4. Tables with Style

```python
# Add sections for grouping
table = Table()
table.add_row("Item 1", "Value 1")
table.add_section()  # Visual separator
table.add_row("Total", "Sum")
```

### 5. Responsive Layouts

```python
# Use Layout for complex UIs
layout = Layout()
layout.split_row(
    Layout(name="left", ratio=1),
    Layout(name="right", ratio=2)
)
```

---

## Click/Typer Tips

### 1. Use Typer for Simple CLIs

```python
# Typer is simpler for basic CLIs
import typer

def main(name: str, count: int = 1):
    for _ in range(count):
        print(f"Hello {name}")

# Auto-generated help, validation, etc.
```

### 2. Use Click for Complex CLIs

```python
# Click gives more control for complex apps
import click

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {'config': load_config()}

@cli.command()
@click.pass_context
def deploy(ctx):
    config = ctx.obj['config']
```

### 3. Validate Early

```python
# Use constraints in options
@app.command()
def process(
    count: int = typer.Option(..., min=1, max=100),
    ratio: float = typer.Option(..., min=0.0, max=1.0)
):
    pass
```

### 4. Use Enums for Choices

```python
# Better than strings
from enum import Enum

class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"

@app.command()
def deploy(env: Environment):
    if env == Environment.PROD:
        confirm = typer.confirm("Deploy to production?")
```

### 5. Helpful Error Messages

```python
# Provide context in errors
if not file.exists():
    console.print(f"[red]Error:[/red] File not found: {file}")
    console.print("[yellow]Tip:[/yellow] Check the file path")
    raise typer.Exit(1)
```

---

## Pydantic Tips

### 1. Use Field for Validation

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    # Much better than just type hints
    age: int = Field(ge=0, le=150, description="User's age")
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
```

### 2. Custom Validators for Complex Logic

```python
@field_validator('email')
@classmethod
def validate_email(cls, v):
    # Complex validation logic
    if '@' not in v:
        raise ValueError('Invalid email')
    domain = v.split('@')[1]
    if domain in BLOCKED_DOMAINS:
        raise ValueError('Email domain not allowed')
    return v.lower()
```

### 3. Model Validators for Cross-Field Validation

```python
@model_validator(mode='after')
def check_dates(self):
    if self.start_date > self.end_date:
        raise ValueError('start_date must be before end_date')
    return self
```

### 4. Use Computed Fields

```python
@computed_field
@property
def full_name(self) -> str:
    return f"{self.first_name} {self.last_name}"
```

### 5. Settings Management

```python
# Use Pydantic for configuration
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str

    class Config:
        env_file = ".env"

# Auto-loads from environment
settings = Settings()
```

### 6. Serialization Tips

```python
# Include/exclude fields
user.model_dump(exclude={'password'})
user.model_dump(include={'id', 'name'})

# Handle None values
user.model_dump(exclude_none=True)

# Pretty JSON
user.model_dump_json(indent=2)
```

---

## Loguru Tips

### 1. Remove Default Handler

```python
from loguru import logger

# Always remove default first
logger.remove()

# Then add your handlers
logger.add(sys.stderr, level="INFO")
logger.add("app.log", rotation="10 MB")
```

### 2. Use Structured Logging

```python
# Better than string formatting
logger.info("User action", user_id=123, action="login", ip="192.168.1.1")

# Not: logger.info(f"User {user_id} logged in from {ip}")
```

### 3. Catch Decorator for Critical Functions

```python
@logger.catch
def main():
    """Automatically logs unhandled exceptions"""
    app.run()
```

### 4. Context with Bind

```python
# Create contextual logger
request_logger = logger.bind(request_id=request_id)
request_logger.info("Processing request")
request_logger.info("Request completed")
```

### 5. Different Handlers for Different Levels

```python
# Console for INFO+
logger.add(sys.stderr, level="INFO", colorize=True)

# File for DEBUG+
logger.add("debug.log", level="DEBUG", rotation="100 MB")

# Separate error log
logger.add("errors.log", level="ERROR", rotation="50 MB", retention="90 days")
```

### 6. Performance with Lazy Evaluation

```python
# Use lazy formatting for performance
logger.debug("Data: {data}", data=expensive_function())

# Only calls expensive_function() if DEBUG level is enabled
```

### 7. Rotation Strategies

```python
# By size
logger.add("app.log", rotation="500 MB")

# By time
logger.add("app.log", rotation="00:00")  # Midnight
logger.add("app.log", rotation="1 week")

# By count
logger.add("app.log", rotation="1000 lines")

# With retention
logger.add("app.log", rotation="100 MB", retention="30 days")

# With compression
logger.add("app.log", rotation="100 MB", compression="gz")
```

---

## Combining Tools

### 1. CLI + Rich + Loguru

```python
import typer
from rich.console import Console
from loguru import logger

app = typer.Typer()
console = Console()
logger.add("app.log", rotation="10 MB")

@app.command()
def process():
    logger.info("Processing started")
    console.print("[green]Processing...[/green]")
    # Do work
    logger.info("Processing completed")
    console.print("[green]✓[/green] Done!")
```

### 2. Pydantic + Typer

```python
from pydantic import BaseModel
import typer

class Config(BaseModel):
    host: str
    port: int

@app.command()
def deploy(config_file: str):
    with open(config_file) as f:
        config = Config.model_validate_json(f.read())
    # Use validated config
```

### 3. Rich + Pydantic

```python
from pydantic import BaseModel
from rich.table import Table

class User(BaseModel):
    id: int
    name: str

users = [User(id=1, name="Alice"), User(id=2, name="Bob")]

table = Table()
table.add_column("ID")
table.add_column("Name")

for user in users:
    table.add_row(str(user.id), user.name)
```

---

## Performance Tips

### 1. Rich Performance

```python
# For large outputs, use pager
with console.pager():
    console.print(large_text)

# Disable auto-detection for speed
console = Console(force_terminal=True, force_interactive=True)
```

### 2. Pydantic Performance

```python
# Use model_validate for speed (no parsing)
user = User.model_validate(data)

# Not: User(**data)  # Slower

# For bulk operations, use TypeAdapter
from pydantic import TypeAdapter

adapter = TypeAdapter(List[User])
users = adapter.validate_python(data_list)
```

### 3. Loguru Performance

```python
# Disable logging in production
logger.disable("my_module")

# Use filters for fine control
def important_only(record):
    return record["level"].no >= 30  # WARNING and above

logger.add("important.log", filter=important_only)
```

---

## Error Handling

### 1. Graceful Failures

```python
@app.command()
def process(file: Path):
    try:
        data = file.read_text()
        config = Config.model_validate_json(data)
    except FileNotFoundError:
        console.print(f"[red]Error:[/red] File not found: {file}")
        logger.error(f"File not found: {file}")
        raise typer.Exit(1)
    except ValidationError as e:
        console.print(f"[red]Validation Error:[/red]")
        console.print(e)
        logger.error(f"Validation failed: {e}")
        raise typer.Exit(1)
```

### 2. User-Friendly Messages

```python
# Show what went wrong and how to fix it
try:
    validate_config(config)
except ConfigError as e:
    console.print(f"[red]Configuration Error:[/red] {e}")
    console.print("[yellow]Tip:[/yellow] Check your .env file")
    console.print("[dim]Example: DATABASE_URL=postgresql://...[/dim]")
```

---

## Testing Tips

### 1. Mock Rich Output

```python
from rich.console import Console
from io import StringIO

def test_output():
    output = StringIO()
    console = Console(file=output)
    console.print("Hello")
    assert "Hello" in output.getvalue()
```

### 2. Test Pydantic Models

```python
import pytest
from pydantic import ValidationError

def test_user_validation():
    # Valid user
    user = User(name="Alice", age=30)
    assert user.name == "alice"

    # Invalid user
    with pytest.raises(ValidationError):
        User(name="AB", age=200)  # Too short, too old
```

### 3. Test CLI Commands

```python
from typer.testing import CliRunner

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice" in result.output
```

---

## Common Pitfalls

### 1. Rich: Forgetting to Import Console

```python
# ✗ Bad
from rich import print
print("[red]Error[/red]")  # Works but limited

# ✓ Good
from rich.console import Console
console = Console()
console.print("[red]Error[/red]")  # Full features
```

### 2. Pydantic: Mutable Defaults

```python
# ✗ Bad
class User(BaseModel):
    tags: List[str] = []  # Shared across instances!

# ✓ Good
from pydantic import Field
class User(BaseModel):
    tags: List[str] = Field(default_factory=list)
```

### 3. Loguru: Not Removing Default Handler

```python
# ✗ Bad: Double logging
logger.add("app.log")  # Plus default stderr

# ✓ Good
logger.remove()
logger.add("app.log")
```

### 4. Typer: Not Using Type Hints

```python
# ✗ Bad: No validation
@app.command()
def process(count):
    pass

# ✓ Good: Automatic validation
@app.command()
def process(count: int):
    pass
```

---

## Production Checklist

- [ ] Rich: Use Console consistently throughout app
- [ ] Rich: Add progress bars for long operations
- [ ] Rich: Use colors for different message types
- [ ] Typer: Add help text to all commands
- [ ] Typer: Validate all inputs with constraints
- [ ] Typer: Use confirmation for destructive actions
- [ ] Pydantic: Validate all external data
- [ ] Pydantic: Use Settings for configuration
- [ ] Pydantic: Add field descriptions
- [ ] Loguru: Configure separate handlers for different levels
- [ ] Loguru: Use log rotation
- [ ] Loguru: Add structured logging with context
- [ ] Error handling: Catch and log all errors
- [ ] Error handling: Provide helpful error messages
- [ ] Testing: Write tests for validation logic
- [ ] Testing: Test CLI commands
- [ ] Documentation: Add docstrings
- [ ] Documentation: Include usage examples

---

## Quick Reference

### Installation

```bash
pip install rich typer click pydantic pydantic-settings loguru
```

### Minimal Setup

```python
import typer
from rich.console import Console
from pydantic import BaseModel
from loguru import logger
import sys

# Setup
app = typer.Typer()
console = Console()
logger.remove()
logger.add(sys.stderr, level="INFO", colorize=True)
logger.add("app.log", rotation="10 MB")

# Model
class Item(BaseModel):
    name: str
    value: int

# Command
@app.command()
def process(file: str):
    logger.info(f"Processing {file}")
    console.print(f"[green]Processing {file}...[/green]")
    # Do work
    logger.info("Completed")

if __name__ == "__main__":
    app()
```

---

## Additional Resources

- **Rich Documentation**: https://rich.readthedocs.io/
- **Click Documentation**: https://click.palletsprojects.com/
- **Typer Documentation**: https://typer.tiangolo.com/
- **Pydantic Documentation**: https://docs.pydantic.dev/
- **Loguru Documentation**: https://loguru.readthedocs.io/

---

Remember: These tools work best together. Use Rich for beautiful output, Typer/Click for CLI structure, Pydantic for validation, and Loguru for logging. Combined, they create professional, maintainable applications.
