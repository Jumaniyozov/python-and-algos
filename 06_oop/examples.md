# OOP: Examples

## Example 1: Bank Account

```python
class BankAccount:
    """Bank account with encapsulation."""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    @property
    def balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.balance)  # 1500
```

## Example 2: Inheritance

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
```

## Example 3: Magic Methods

```python
from dataclasses import dataclass

@dataclass
class Money:
    amount: float
    currency: str = "USD"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"${self.amount:.2f} {self.currency}"

m1 = Money(10.50)
m2 = Money(5.25)
print(m1 + m2)  # $15.75 USD
```

See solutions.md for more examples!
