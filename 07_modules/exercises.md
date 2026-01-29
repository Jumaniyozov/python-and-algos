# Modules and Packages: Practice Exercises

## Exercise 1: Create a Math Module
Create a module `my_math.py` with functions for:
- `square(x)` - return x²
- `cube(x)` - return x³
- `factorial(n)` - return n!

Include a `__main__` section to test the functions.

## Exercise 2: Temperature Converter Module
Create `temperature.py` with:
- `celsius_to_fahrenheit(c)`
- `fahrenheit_to_celsius(f)`
- `celsius_to_kelvin(c)`
- `kelvin_to_celsius(k)`

Export only the conversion functions, not any helper functions.

## Exercise 3: Simple Package
Create a package `calculator` with:
```
calculator/
    __init__.py
    basic.py  # add, subtract, multiply, divide
    advanced.py  # power, sqrt, factorial
```

Make all functions importable from the package level:
```python
from calculator import add, power
```

## Exercise 4: Relative Imports
Create:
```
myproject/
    __init__.py
    core.py
    utils/
        __init__.py
        helpers.py
```

In `core.py`, import from `helpers.py` using relative imports.

## Exercise 5: Module with __all__
Create a module that:
- Has 3 public functions (in `__all__`)
- Has 2 private functions (not in `__all__`)
- Test that `from module import *` only imports public functions

## Exercise 6: Plugin Loader
Create a plugin system that:
- Has a `plugins/` directory
- Automatically discovers and loads all `.py` files in `plugins/`
- Each plugin has a `register()` function that gets called

## Exercise 7: Lazy Import
Create a module with a function that:
- Only imports heavy libraries (like pandas) when called
- Measure the difference in import time

## Exercise 8: Singleton Module
Create a module that maintains state:
- A counter that increments each time a function is called
- The counter should persist across different imports in the same program

## Exercise 9: Fix Circular Import
Given two modules with circular dependency:
```python
# user.py
from post import Post

class User:
    def create_post(self):
        return Post(self)

# post.py
from user import User

class Post:
    def __init__(self, user):
        self.user = user
```

Fix the circular import.

## Exercise 10: Package with Subpackages
Create:
```
data_processor/
    __init__.py
    readers/
        __init__.py
        csv_reader.py
        json_reader.py
    writers/
        __init__.py
        csv_writer.py
        json_writer.py
```

Make readers and writers accessible from the main package.

## Challenge 1: Dynamic Module Loading
Create a function `load_module_from_path(path)` that:
- Takes a file path
- Loads the module dynamically
- Returns the module object
- Works even if the path is not in sys.path

## Challenge 2: Module Hot Reload
Create a system that:
- Watches a module file for changes
- Automatically reloads the module when it changes
- Updates all references to the module

## Challenge 3: Namespace Package
Create a namespace package spread across two directories:
```
location1/
    mypkg/
        module1.py

location2/
    mypkg/
        module2.py
```

Both should be importable as `from mypkg import module1, module2`.

See solutions.md for answers!
