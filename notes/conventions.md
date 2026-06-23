# Repository Conventions

This file defines the naming, documentation, and commit conventions for this repository.

## Folder Naming

Use lowercase names with hyphens.

Good:

```text
week-01-core-foundations
day-01-python-basics
student-result-management
```

Avoid:

```text
Week 1
Day 1
Python Basics
week1
```

## File Naming

Use clear and simple lowercase file names.

Common files:

```text
README.md
notes.md
practice.md
exercises.py
main.py
requirements.txt
```

## Documentation Rules

Each important folder should explain its purpose.

Use:

- Root `README.md` for overall repo purpose.
- Language `README.md` for language-specific learning purpose.
- Week `README.md` for weekly focus.
- Day `README.md` for daily topic overview.
- `notes.md` for actual learning notes.
- `practice.md` for exercises and small projects.

## Daily Folder Structure

Each learning day should usually follow this structure:

```text
day-01-topic-name/
├── README.md
├── notes.md
├── practice.md
└── exercises.py
```

If a day includes a mini-project, add:

```text
mini_project.py
```

## Project Folder Structure

Each project should usually follow this structure:

```text
project-name/
├── README.md
├── main.py
└── notes.md
```

For larger projects, extra folders can be added:

```text
data/
utils/
tests/
```

## Commit Message Style

Use simple and meaningful commit messages.

Examples:

```bash
git commit -m "Complete Python day 1 basics"
git commit -m "Add string practice exercises"
git commit -m "Build student result mini project"
git commit -m "Update Python progress tracker"
```

## Main Rule

Keep the repo clean, practical, and easy to understand.
