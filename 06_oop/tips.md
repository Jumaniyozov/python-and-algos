# OOP: Tips and Gotchas

## Tip 1: Prefer Composition Over Inheritance

**Inheritance (tight coupling)**:
```python
class Car(Engine, Wheels, Seats):  # Complex!
    pass
```

**Composition (loose coupling)**:
```python
class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]
```

## Tip 2: Use Dataclasses

**Without dataclass**:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

**With dataclass**:
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

## Gotcha 1: Mutable Class Variables

**Bad**:
```python
class MyClass:
    items = []  # Shared across ALL instances!

    def add_item(self, item):
        self.items.append(item)

a = MyClass()
b = MyClass()
a.add_item(1)
print(b.items)  # [1] - Unexpected!
```

**Good**:
```python
class MyClass:
    def __init__(self):
        self.items = []  # Instance variable
```

## Gotcha 2: Private Variables

Python has no true private variables. `__name` is name mangled but still accessible:

```python
class MyClass:
    def __init__(self):
        self.__private = 42

obj = MyClass()
# obj.__private  # AttributeError
obj._MyClass__private  # 42 - name mangled
```

Use single underscore `_name` to indicate "internal use".

## Best Practices

- ✅ Use `@dataclass` for data containers
- ✅ Implement `__repr__` for debugging
- ✅ Use properties for computed values
- ✅ Prefer composition over inheritance
- ✅ Use ABC for interfaces
- ✅ Follow SOLID principles
- ❌ Don't use mutable class variables
- ❌ Don't make everything a class
- ❌ Don't over-engineer

See examples.md for patterns!
