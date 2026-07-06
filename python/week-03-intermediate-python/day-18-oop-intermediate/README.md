# Day 18: Classes in Practical Projects

## Learning Goals

- Strengthen the class, object, constructor, attribute, and method concepts from Day 17.
- Turn a real-world record into a small, focused class.
- Clean and validate data before allowing an object to use it.
- Use methods to change an object's state safely.
- Add a simple `__str__()` method for readable object output.
- Decide which behavior belongs inside a class and which belongs in the main program.
- Create and use multiple practical objects without inheritance.
- Build a small Library Lending System using simple classes.

---

## Quick Review From Day 17

Answer these questions from memory before reading the notes:

1. What is the difference between a class and an object?
2. When does `__init__()` run?
3. What does `self` refer to?
4. What is an instance attribute?
5. How is an instance method different from a normal function?
6. Why should a calculation method usually return its result?
7. If two objects come from the same class, do they share their instance values?
8. How did the Day 17 `Student` class combine data and behavior?

Open the Day 17 code only after writing your answers. Active recall makes the
new lesson much easier to absorb.

---

## Study Notes

### From Syntax to Practical Class Design

Day 17 taught how classes work. Day 18 focuses on deciding what a useful class
should contain.

A practical class usually has:

- a clear purpose
- attributes that describe one object
- methods that use or update those attributes
- validation that protects the object from invalid changes
- readable output

For example, an inventory item has data and behavior:

```text
Data:
- name
- price
- quantity

Behavior:
- calculate stock value
- add stock
- sell stock
- display a summary
```

That is a good reason to create a class.

### Model One Clear Thing

A class should represent one clear idea.

```python
class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```

This class models one inventory record. Each object represents one item:

```python
keyboard = InventoryItem("Keyboard", 2499, 8)
mouse = InventoryItem("Mouse", 899, 15)
```

Avoid creating one giant class responsible for inventory, login, reports,
student results, and every other part of the program.

### Clean Constructor Input

The string-cleaning skills from Day 2 are still useful inside classes.

```python
class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = " ".join(name.split()).title()
        self.price = price
        self.quantity = quantity
```

Now messy input such as `"  wireless   mouse "` becomes
`"Wireless Mouse"`.

The constructor should establish a sensible starting state. The surrounding
program can validate user input before creating the object:

```python
if name and price >= 0 and quantity >= 0:
    item = InventoryItem(name, price, quantity)
else:
    print("Invalid inventory details.")
```

For now, use straightforward conditions. Exceptions are covered properly on
Day 12 when you return to the deferred lessons.

### Query Methods and Command Methods

Some methods answer a question without changing the object:

```python
def calculate_stock_value(self):
    return self.price * self.quantity


def is_in_stock(self):
    return self.quantity > 0
```

Other methods change the object's state:

```python
def restock(self, amount):
    self.quantity = self.quantity + amount
```

It helps to recognize the difference:

- a **query method** returns information
- a **command method** changes the object

You do not need to memorize these labels. Focus on whether a method changes an
attribute or only returns a result.

### Protect State Changes With Conditions

Methods should reject changes that would make the object's state invalid.

```python
def sell(self, amount):
    if amount <= 0:
        return False

    if amount > self.quantity:
        return False

    self.quantity = self.quantity - amount
    return True
```

The method returns `True` when the sale succeeds and `False` when it fails.
The main program can decide which message to display:

```python
sale_completed = keyboard.sell(2)

if sale_completed:
    print("Sale completed.")
else:
    print("Sale could not be completed.")
```

This reuses conditions, Boolean values, parameters, and return values from
Days 4–6.

### A Light Introduction to `__str__()`

Printing an ordinary object does not initially show useful information:

```python
print(keyboard)
```

Python may display something similar to:

```text
<__main__.InventoryItem object at 0x...>
```

`__str__()` tells Python how the object should look as readable text:

```python
class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} | INR {self.price:.2f} | Stock: {self.quantity}"
```

Now this:

```python
print(keyboard)
```

can display:

```text
Keyboard | INR 2499.00 | Stock: 8
```

Important rules:

- `__str__()` must return a string
- it should not call `print()` itself
- use it for a short human-readable summary
- keep detailed reports in a normal method

The double-underscore name is intentional. Methods like `__init__()` and
`__str__()` are often called dunder methods.

### Keep Input Outside the Class

Prefer collecting terminal input in the main program:

```python
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))

item = InventoryItem(item_name, item_price, 0)
```

Avoid placing `input()` directly inside `__init__()`. Passing values into the
constructor makes the class easier to reuse later in a terminal app, test, web
API, or notebook.

### Keep Display Decisions Outside When Possible

A class can return information:

```python
if item.sell(2):
    print("Sale completed.")
else:
    print("Not enough stock.")
```

This is usually more reusable than making `sell()` ask for input and print
every message itself.

For a beginner project, a dedicated `print_report()` method is still fine when
formatted terminal output is one of the class's clear responsibilities.

### Work With Multiple Objects

One class can model many independent records:

```python
keyboard = InventoryItem("Keyboard", 2499, 8)
mouse = InventoryItem("Mouse", 899, 15)

keyboard.sell(2)

print(keyboard)  # quantity is now 6
print(mouse)     # quantity is still 15
```

Methods affect only the object used to call them.

### Choosing Class Responsibilities

Ask these questions when designing a class:

1. What real-world thing does this class represent?
2. Which values describe one object?
3. Which calculations use those values?
4. Which actions should update those values?
5. Which invalid changes should the class reject?
6. What short text should `print(object)` display?

If a method has nothing to do with the object's attributes, it may belong
outside the class as a normal function.

### Today Is Not About Inheritance

The existing `exercises/youtube/` folder contains earlier experiments with:

- inheritance
- encapsulation and properties
- polymorphism
- class and static methods
- multiple inheritance

Those files are preserved as optional reference material, but they are not
required for today's checklist. Day 18 follows the repository roadmap:
practical record classes and a light introduction to `__str__()`.

Master simple classes before adding relationships between parent and child
classes.

---

## Code-Along

The guided `main.py` builds an inventory item step by step:

1. Model an item with instance attributes.
2. Clean constructor input.
3. Calculate stock value with a query method.
4. Restock and sell through command methods.
5. Reject invalid state changes.
6. Add readable `__str__()` output.
7. Prove that multiple objects remain independent.

Run it from the repository root:

```bash
python3 python/week-03-intermediate-python/day-18-oop-intermediate/main.py
```

After the first run:

1. Add a third item.
2. Attempt to sell more units than it has.
3. Restock it and try the sale again.
4. Predict every quantity before running the file.

---

## Daily Exercises

Use `main.py` for the guided lesson and the files in `exercises/` for
independent practice.

### Exercise 1: Product Record

Create a `Product` class containing:

- name
- category
- price
- discount percentage
- a method that calculates the discounted price
- a method that checks whether the product is affordable for a given budget
- a `__str__()` method

Create two products and print their original and discounted prices.

File: `exercises/01_product_record.py`

### Exercise 2: Bank Account

Create a `BankAccount` class containing:

- account holder
- account number
- balance
- a method to deposit a valid positive amount
- a method to withdraw only when sufficient funds exist
- a method that returns the current balance
- a `__str__()` method that does not expose the full account number

Test successful and unsuccessful transactions.

File: `exercises/02_bank_account.py`

### Exercise 3: Library Book

Create a `LibraryBook` class containing:

- title
- author
- book ID
- availability status
- a method to borrow the book
- a method to return the book
- a `__str__()` method

Test borrowing the same book twice and returning it twice.

File: `exercises/03_library_book.py`

### Mini-Project: Library Lending System

Build a small system with:

- a `LibraryBook` class
- a `LibraryMember` class
- two books
- two members
- methods that borrow and return a book
- validation that prevents unavailable books from being borrowed
- readable `__str__()` output for books and members

Keep the design simple. Do not use inheritance, private attributes, properties,
static methods, or class methods.

File: `exercises/04_library_lending_system.py`

---

## AI/ML Preparation

Practical class design prepares you to understand library objects later:

- a model object stores configuration and learned state
- `fit()` changes the model's state
- `predict()` returns information using that state
- readable object summaries help inspect tools and datasets
- validation prevents invalid settings from entering a workflow

The useful habit is not “put everything in a class.” It is grouping related
data and behavior when that makes the program clearer.

---

## Common Mistakes

- Creating a class when a small function would be enough.
- Giving one class too many unrelated responsibilities.
- Putting every `input()` and `print()` call inside the class.
- Updating an attribute before validating the requested change.
- Allowing quantity, balance, price, or hours to become negative.
- Forgetting to use `self.` when reading or updating an attribute.
- Returning a number or printing inside `__str__()` instead of returning text.
- Calling `object.__str__()` directly instead of using `str(object)` or
  `print(object)`.
- Accidentally changing one object while expecting another object to change.
- Jumping into inheritance before simple object design feels comfortable.

---

## End-of-Day Checklist

- [ ] Answered the Day 17 review questions from memory.
- [ ] Read the study notes.
- [ ] Ran and modified `main.py`.
- [ ] Designed a class that models one clear record.
- [ ] Cleaned or validated constructor data.
- [ ] Wrote a query method that returns information.
- [ ] Wrote a command method that safely changes an attribute.
- [ ] Prevented at least one invalid state change.
- [ ] Added a `__str__()` method that returns readable text.
- [ ] Created multiple independent objects.
- [ ] Completed at least three exercise scripts.
- [ ] Built the Library Lending System mini-project.
- [ ] Updated `python/progress.md` with confidence and blockers.
- [ ] Committed the day using Conventional Commit style.
