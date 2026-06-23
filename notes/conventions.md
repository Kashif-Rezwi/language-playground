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
main.py
setup.md
requirements.txt
```

## Documentation Rules

Each important folder should explain its purpose.

Use:

- Root `README.md` for overall repo purpose.
- Language `README.md` (e.g., `python/README.md`) for language-specific curriculum and roadmap.
- Week `README.md` for weekly overview and project description.
- Day `README.md` for daily learning goals, study notes, and exercises prompts.

## Daily Folder Structure

To minimize documentation overhead and maximize active coding time, each learning day follows a strict 2-file structure:

```text
day-XX-topic-name/
├── README.md                  # Study notes, objectives, and exercise prompts
└── main.py                    # Solution code, code-along examples, and exercises
```

All notes are written directly in the local `README.md`, and all executable Python code resides inside `main.py`.

## Project Folder Structure

Weekly projects and the final capstone project live inside the centralized `python/projects/` directory to avoid code fragmentation:

```text
python/projects/project-name/
├── README.md                  # Project specification and requirements
├── main.py                    # Project entry point and execution script
├── utils.py                   # Helper functions (optional)
└── tests/                     # Unit tests (optional, using pytest)
```

The weekly project folder (e.g., `day-07-week-01-project/`) must only contain a single `README.md` file that specifies the project requirements and links to the centralized directory.

## Commit Message Style

Use standard Conventional Commit prefixes to organize your repository history:

* `feat(day-XX):` Add exercise solutions or daily practice code (e.g., `feat(day-05): complete loop exercises`)
* `docs(day-XX):` Add or update study notes (e.g., `docs(day-02): add string formatting notes`)
* `feat(project-X):` Add features to weekly or capstone projects (e.g., `feat(project-1): implement grade scoring logic`)
* `fix(project-X):` Fix bugs in projects or exercises (e.g., `fix(project-2): resolve calculation overflow`)
* `test(day-XX):` Add or update unit tests (e.g., `test(day-19): add validation tests`)
* `refactor(day-XX):` Restructure or optimize code without changing behavior (e.g., `refactor(day-06): simplify functions`)

## Main Rule

Keep the repo clean, practical, and easy to understand.
