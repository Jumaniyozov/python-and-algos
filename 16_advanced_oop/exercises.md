# Exercises: Advanced OOP & Metaclasses

## Exercise 1: Attribute Logger Metaclass (Easy)
Create a metaclass `LoggerMeta` that prints a message every time an attribute is set on an instance of a class using that metaclass.

**Requirements:**
- Override `__setattr__` in the metaclass
- Print the attribute name and value
- Create a sample class using this metaclass

## Exercise 2: Required Methods Validator (Easy)
Create a class decorator `@requires_methods` that validates a class has specific methods defined.

**Requirements:**
- Take method names as arguments
- Raise `TypeError` if any method is missing
- Test with valid and invalid classes

## Exercise 3: Cached Property Descriptor (Medium)
Implement a `CachedProperty` descriptor that:
- Computes the value on first access
- Caches the result
- Allows clearing the cache via a method
- Tracks how many times the property was computed

**Example usage:**
```python
class Example:
    @CachedProperty
    def expensive_computation(self):
        return sum(range(1000000))
```

## Exercise 4: Type-Safe Metaclass (Medium)
Create a metaclass that enforces type annotations for all attributes in a class.

**Requirements:**
- Check that all attributes have type hints
- Validate attribute values match their type hints on assignment
- Raise appropriate errors for violations

## Exercise 5: Plugin Manager (Medium)
Build a complete plugin system using `__init_subclass__`:
- Base class `Plugin` with plugin registration
- Support for enabling/disabling plugins
- Priority-based plugin execution order
- Method to execute all enabled plugins

**Example:**
```python
class EmailPlugin(Plugin, name="email", priority=1):
    def execute(self, data):
        return f"Emailing: {data}"
```

## Exercise 6: Immutable Class Decorator (Medium)
Create a `@immutable` decorator that makes all attributes of a class read-only after initialization.

**Requirements:**
- Allow setting attributes in `__init__`
- Prevent modification after initialization
- Prevent deletion of attributes
- Raise appropriate exceptions

## Exercise 7: Validated Dictionary Descriptor (Medium)
Implement a descriptor `ValidatedDict` that:
- Only accepts dictionary values
- Validates keys match a specified type
- Validates values match a specified type
- Provides helpful error messages

**Example:**
```python
class Config:
    settings = ValidatedDict(key_type=str, value_type=int)
```

## Exercise 8: Auto-documentation Metaclass (Hard)
Create a metaclass that automatically generates documentation for a class:
- Extracts all method signatures
- Collects all docstrings
- Generates a formatted `__doc__` string
- Lists all public methods and attributes

## Exercise 9: ORM Field System (Hard)
Build a simplified ORM system with:
- Field descriptors: `CharField`, `IntegerField`, `FloatField`
- Metaclass that collects field definitions
- `Model` base class with `save()` and `to_dict()` methods
- Field validation on assignment
- Support for default values

**Example usage:**
```python
class User(Model):
    name = CharField(max_length=50)
    age = IntegerField(min_value=0, max_value=150)
    email = CharField()

user = User(name="Alice", age=30, email="alice@example.com")
```

## Exercise 10: State Machine with Metaclass (Hard)
Create a state machine framework using a metaclass:
- Define states as class attributes
- Define valid transitions
- Prevent invalid state transitions
- Track state history
- Emit events on state changes

**Example:**
```python
class Door(StateMachine):
    states = ['open', 'closed', 'locked']
    transitions = {
        'open': ['closed'],
        'closed': ['open', 'locked'],
        'locked': ['closed']
    }
    initial_state = 'closed'
```

## Exercise 11: Memoization Descriptor (Medium)
Create a `Memoized` descriptor that caches method results based on arguments.

**Requirements:**
- Cache results per unique argument combination
- Support both positional and keyword arguments
- Provide a method to clear the cache
- Handle unhashable arguments gracefully

## Exercise 12: Abstract Property Pattern (Medium)
Implement an abstract property pattern that:
- Requires subclasses to define certain properties
- Validates property types
- Supports both getter and setter as abstract
- Works with the ABC module

## Exercise 13: Dynamic Model Factory (Hard)
Create a factory function that generates model classes from a schema:

**Requirements:**
- Accept a schema dictionary: `{'field_name': type}`
- Generate appropriate descriptors for each field
- Add validation based on type
- Include `__init__`, `__repr__`, and `__eq__` methods
- Support nested models

**Example:**
```python
User = create_model('User', {
    'name': str,
    'age': int,
    'email': str
})
```

## Exercise 14: Method Call Counter (Easy)
Create a class decorator that counts how many times each method is called.

**Requirements:**
- Track calls per method
- Provide a `get_stats()` class method
- Don't count special methods (starting with `__`)
- Reset functionality

## Exercise 15: Multi-dispatch System (Hard)
Implement a simple multiple dispatch system using a metaclass:
- Allow multiple methods with the same name but different signatures
- Dispatch based on argument types
- Raise error if no matching signature found
- Support inheritance

**Example:**
```python
class Calculator(metaclass=MultiDispatchMeta):
    def add(self, a: int, b: int):
        return a + b

    def add(self, a: str, b: str):
        return a + b

calc = Calculator()
print(calc.add(1, 2))      # 3
print(calc.add("a", "b"))  # "ab"
```

## Bonus Challenge: Complete Framework

Build a mini web framework that combines:
- Metaclass for route registration
- Descriptors for request/response handling
- Class decorators for middleware
- Abstract base classes for views
- Dynamic class generation for model binding

This should demonstrate mastery of all advanced OOP concepts covered in this chapter.

## Testing Your Solutions

For each exercise:
1. Write comprehensive test cases
2. Test edge cases and error conditions
3. Verify memory efficiency
4. Check that error messages are helpful
5. Ensure code is well-documented

## Hints

- **Exercise 1-2**: Start simple, focus on the basic mechanism
- **Exercise 3**: Use `__set_name__` to get the attribute name
- **Exercise 4-5**: Research how type hints are stored (`__annotations__`)
- **Exercise 6**: Consider using `__setattr__` and tracking initialization state
- **Exercise 7**: Look at how dictionary key/value pairs are validated
- **Exercise 8-9**: Break down into smaller components, test incrementally
- **Exercise 10**: State machines benefit from clear state tracking
- **Exercise 11**: Use `functools.wraps` and careful cache key generation
- **Exercise 12**: Combine `@property`, `@abstractmethod`, and ABC
- **Exercise 13**: This is essentially building a mini version of `dataclasses`
- **Exercise 14**: Use a wrapper function to intercept method calls
- **Exercise 15**: Research function signature inspection with `inspect` module

Good luck! These exercises will significantly deepen your understanding of Python's advanced features.
