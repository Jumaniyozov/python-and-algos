# Object-Oriented Programming: Theory

## 6.1 Classes and Objects

```python
class Dog:
    """A simple class."""
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        """Initialize instance."""
        self.name = name  # Instance variable
        self.age = age

    def bark(self):
        """Instance method."""
        return f"{self.name} says woof!"

    @classmethod
    def get_species(cls):
        """Class method - receives class."""
        return cls.species

    @staticmethod
    def is_valid_age(age):
        """Static method - no self/cls."""
        return 0 <= age <= 25

# Create instance
buddy = Dog("Buddy", 3)
buddy.bark()  # "Buddy says woof!"
Dog.get_species()  # "Canis familiaris"
Dog.is_valid_age(5)  # True
```

## 6.2 Inheritance and MRO

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Multiple inheritance
class Pet:
    def __init__(self, owner):
        self.owner = owner

class PetDog(Dog, Pet):  # Multiple inheritance
    def __init__(self, name, owner):
        Dog.__init__(self, name)
        Pet.__init__(self, owner)

# MRO (Method Resolution Order)
PetDog.__mro__
# (PetDog, Dog, Animal, Pet, object)
```

### super()

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent init
        self.age = age
```

## 6.3 Magic Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v1 + v2  # Vector(4, 6)
v1 == v2  # False
len(v1)  # 2
v1[0]  # 1
```

### Common Magic Methods

- `__init__`, `__del__`: Constructor/destructor
- `__repr__`, `__str__`: String representation
- `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`: Comparison
- `__add__`, `__sub__`, `__mul__`, `__truediv__`: Arithmetic
- `__len__`, `__getitem__`, `__setitem__`: Container emulation
- `__call__`: Make object callable
- `__enter__`, `__exit__`: Context manager

## 6.4 Properties and Descriptors

### Properties

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set celsius with validation."""
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property."""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
temp.celsius  # 25 (calls getter)
temp.celsius = 30  # Calls setter
temp.fahrenheit  # 86.0 (computed)
```

### Descriptors

```python
class Positive:
    """Descriptor that ensures positive values."""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Product:
    price = Positive()
    quantity = Positive()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
```

## 6.5 Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class."""
    @abstractmethod
    def area(self):
        """Must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate ABC
# shape = Shape()  # TypeError!
rect = Rectangle(5, 3)  # OK
```

## 6.6 Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    """Automatic __init__, __repr__, __eq__."""
    x: int
    y: int

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown"  # Default value
    friends: list = field(default_factory=list)  # Mutable default

p = Point(10, 20)
print(p)  # Point(x=10, y=20)

# With post-init processing
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # Not in __init__

    def __post_init__(self):
        self.area = self.width * self.height
```

## 6.7 Protocols (PEP 544)

```python
from typing import Protocol

class Drawable(Protocol):
    """Structural subtyping - duck typing with type hints."""
    def draw(self) -> None:
        ...

class Circle:
    """Implements Drawable protocol (no explicit inheritance)."""
    def draw(self) -> None:
        print("Drawing circle")

def render(obj: Drawable):
    """Accepts anything with draw() method."""
    obj.draw()

render(Circle())  # OK - has draw() method
```

## 6.8 Metaclasses (Advanced)

```python
class Meta(type):
    """Metaclass that customizes class creation."""
    def __new__(mcs, name, bases, attrs):
        # Add timestamp to all classes
        attrs['created_at'] = time.time()
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

MyClass.created_at  # Timestamp
```

## Key Concepts

1. **Encapsulation**: Bundle data and methods
2. **Inheritance**: Reuse code from parent classes
3. **Polymorphism**: Same interface, different implementations
4. **Abstraction**: Hide complexity, show essentials
5. **Composition**: Build complex objects from simple ones

## Best Practices

- Use `@dataclass` for simple data containers
- Prefer composition over inheritance
- Use ABC for interfaces
- Keep classes focused (Single Responsibility)
- Use properties for computed values
- Implement `__repr__` for debugging
- Use protocols for duck typing with type hints

See examples.md for practical code!
