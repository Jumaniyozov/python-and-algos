# OOP: Solutions

## Solution 1: Rectangle

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())  # 15
```

## Solution 2: Vehicle Inheritance

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} starting..."

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
```

## Solution 3: Fraction Class

```python
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        g = gcd(numerator, denominator)
        self.num = numerator // g
        self.den = denominator // g

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __str__(self):
        return f"{self.num}/{self.den}"
```

## Solution 4: Circle Properties

```python
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self._radius
```

## Solution 5: Dataclass

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

# Automatic __init__, __repr__, __eq__
```

## Solution 6: Payment ABC

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Charged ${amount} to card {self.card_number}"

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Charged ${amount} to PayPal {self.email}"
```

More solutions in complete curriculum!
