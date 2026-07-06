# Day 17: Object-Oriented Programming Basics

## Learning Goals

- Understand why object-oriented programming groups related data and behavior.
- Explain the difference between a class and an object.
- Create a class using the `class` keyword.
- Initialize objects with the `__init__` constructor.
- Use `self` to store and access instance attributes.
- Define and call instance methods.
- Create multiple independent objects from one class.
- Refactor the student-result logic from Days 4–6 into a simple `Student` class.

---

## Study Notes

### Why OOP?

The function-based student system from Day 6 keeps data in separate variables:

```python
student_name = "Kashif"
math_marks = 85
science_marks = 90
english_marks = 78
```

As a program grows, it becomes harder to remember which values and functions
belong together. Object-oriented programming (OOP) lets us group one student's
data and behavior into one object.

```python
student = Student("Kashif", 85, 90, 78)

print(student.name)
print(student.calculate_percentage())
```

Use OOP when a program contains clear things—such as students, books, products,
or bank accounts—that have both data and actions.

### Classes and Objects

A **class** is a blueprint. An **object** is one value created from that
blueprint.

```python
class Student:
    pass


student_1 = Student()
student_2 = Student()
```

`Student` is the class. `student_1` and `student_2` are separate objects, also
called instances.

Class names normally use `PascalCase`, while variables and methods use
`snake_case`.

### The `__init__` Constructor

`__init__` runs automatically whenever a new object is created. It gives the
object its starting attributes.

```python
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number


student = Student("Kashif", "PY-017")
```

In the call above:

- `"Kashif"` becomes `name`
- `"PY-017"` becomes `roll_number`
- Python supplies `self` automatically

The double underscores in `__init__` are intentional.

### Understanding `self`

`self` means “this current object.” It lets each object keep its own values.

```python
class Student:
    def __init__(self, name):
        self.name = name


student_1 = Student("Aarav")
student_2 = Student("Meera")

print(student_1.name)  # Aarav
print(student_2.name)  # Meera
```

`self.name` is an instance attribute. Each `Student` object receives its own
copy.

`self` must be the first parameter of every instance method, but it is not
written when calling the method:

```python
student_1.show_profile()
```

### Instance Attributes

Attributes store an object's data and are accessed with dot notation.

```python
class Course:
    def __init__(self, title, duration_days):
        self.title = title
        self.duration_days = duration_days


python_course = Course("Python Foundations", 30)

print(python_course.title)
print(python_course.duration_days)
```

An attribute can be updated:

```python
python_course.duration_days = 35
```

For Day 17, keep attributes simple and public. Encapsulation and properties are
later topics.

### Instance Methods

An instance method is a function inside a class that works with an object's
attributes.

```python
class Course:
    def __init__(self, title, completed_days):
        self.title = title
        self.completed_days = completed_days

    def show_progress(self):
        print(f"{self.title}: {self.completed_days} days completed")

    def add_completed_day(self):
        self.completed_days = self.completed_days + 1


course = Course("Python Foundations", 6)
course.show_progress()
course.add_completed_day()
course.show_progress()
```

Methods can print output, update attributes, or return calculated values.

### Returning Values From Methods

The same `return` rule from Day 6 applies to methods.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rectangle = Rectangle(8, 5)
area = rectangle.calculate_area()
print(f"Area: {area}")
```

Return a value when another part of the program needs to reuse the result.

### Multiple Independent Objects

One class can create many objects:

```python
student_1 = Student("Aarav", "PY-001")
student_2 = Student("Meera", "PY-002")
```

Changing `student_1.name` does not change `student_2.name`. Each object keeps
its own instance attributes.

### Functions Versus Methods

```python
def clean_name(name):
    return name.strip().title()
```

`clean_name()` is a function because it exists by itself.

```python
class Student:
    def clean_name(self):
        return self.name.strip().title()
```

`clean_name()` is now a method because it belongs to `Student` and is called
through an object:

```python
student.clean_name()
```

Methods are useful when the behavior naturally belongs to the object's data.

---

## Code-Along

Run `main.py` and study it in this order:

1. Create a basic class and object.
2. Add a constructor and instance attributes.
3. Add methods that return and update values.
4. Create two independent objects.
5. Build a small `Student` result model using skills from Days 1–6.

Run it from the repository root:

```bash
python3 python/week-03-intermediate-python/day-17-oop-basics/main.py
```

Then modify one object, add a third object, and predict the output before
running it again.

---

## Daily Exercises

Use `main.py` for the guided lesson. Use the files in `exercises/` as
independent practice.

### Exercise 1: Classes and Objects

Create a `Car` class with `brand` and `model` attributes. Create two different
cars and print their attributes.

Starter practice:
`exercises/youtube/01_classes_and_objects.py`

### Exercise 2: Instance Methods

Add a `full_name()` method to `Car`. It should return the brand and model as one
formatted string.

Starter practice:
`exercises/youtube/02_instance_methods.py`

### Exercise 3: Book Information

Create a `Book` class containing:

- title
- author
- page count
- a method that returns a formatted book summary
- a method that returns whether the book has more than 300 pages

Create at least two books to prove their attributes are independent.

### Exercise 4: Study Session Tracker

Create a `StudySession` class containing:

- topic
- planned hours
- completed hours starting at `0`
- a method to add completed hours
- a method to return the remaining hours
- a method to print a progress summary

Reuse loops, conditions, numeric formatting, and return values from Days 3–6.

### Mini-Project: OOP Student Result System

Create a `Student` class containing:

- student name
- roll number
- Mathematics marks
- Science marks
- English marks

Add instance methods that:

- validate all marks
- calculate total marks
- calculate percentage
- return the grade
- check whether any subject was failed
- return `PASSED` or `FAILED`
- print a formatted student report

Create at least two `Student` objects and print both reports. This is the
object-oriented version of the function-based result system from Day 6.

---

## AI/ML Preparation

OOP appears throughout data and machine-learning libraries:

- a dataset can be represented by an object
- a model object can store learned values
- methods such as `fit()`, `predict()`, and `transform()` perform behavior
- separate model objects keep their own settings and results

You do not need advanced OOP for AI/ML yet. The goal is to recognize the
class-object-method pattern when libraries introduce it.

---

## Common Mistakes

- Forgetting the colon after a class or method definition.
- Forgetting `self` as the first parameter of `__init__` or an instance method.
- Writing `name = name` instead of `self.name = name`.
- Calling `Student.__init__()` directly instead of creating `Student(...)`.
- Passing `self` manually when calling `student.show_profile()`.
- Confusing the class `Student` with an object such as `student_1`.
- Printing inside every method when a returned value is needed later.
- Accidentally using one shared variable instead of separate instance attributes.
- Moving into inheritance or other advanced OOP before these basics feel natural.

---

## End-of-Day Checklist

- [ ] Answered the Days 1–6 review questions from memory.
- [ ] Read the study notes.
- [ ] Ran and modified `main.py`.
- [ ] Explained class versus object in my own words.
- [ ] Created a class with an `__init__` constructor.
- [ ] Explained what `self` refers to.
- [ ] Created and accessed instance attributes.
- [ ] Wrote methods that return and update values.
- [ ] Created multiple independent objects from one class.
- [ ] Completed at least three exercise scripts.
- [ ] Built the OOP Student Result System mini-project.
- [ ] Updated `python/progress.md` with confidence and blockers.
- [ ] Committed the day using Conventional Commit style.
