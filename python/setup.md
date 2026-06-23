# Python Setup Guide

This file contains setup commands, command line (CLI) basics, Git commands, and package management workflows for learning Python in this repository.

---

## 1. Command Line (CLI) Basics

Before running Python scripts, make sure you can navigate directories via your terminal:

* **Print working directory:**
  * macOS/Linux: `pwd`
  * Windows (PowerShell): `Get-Location` or `pwd`
* **List contents of directory:**
  * macOS/Linux/Windows: `ls` (or `dir` on CMD)
* **Change directory:**
  * Go to `python/` directory: `cd python`
  * Move up one folder: `cd ..`
* **Create a new folder:**
  * `mkdir day-01-python-basics`

---

## 2. Git & Version Control Basics

Track your daily progress by running these commands from the repository root:

* **Check status of your workspace:**
  * `git status`
* **Stage changes for commit:**
  * Stage a specific file: `git add python/week-01-core-foundations/day-01-python-basics/main.py`
  * Stage all changes: `git add .`
* **Commit staged changes:**
  * Use the Conventional Commit prefix: `git commit -m "feat(day-01): complete basics exercises"`
* **Push changes to GitHub:**
  * `git push origin main`

---

## 3. Python Version Verification

Verify that Python 3 is installed:

```bash
python3 --version
```
*(On Windows, you may need to use `python --version`)*

---

## 4. Virtual Environment Workflow

Always run external packages within a virtual environment. Keep the `.venv` inside the `python/` directory.

### Create the Environment
From the `python/` folder:
```bash
python3 -m venv .venv
```

### Activate the Environment
Before installing packages or running scripts that require dependencies, activate the virtual environment:

* **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

> [!IMPORTANT]
> **Active Verification:** Always verify that your terminal prompt shows `(.venv)` before running `pip install` commands. This confirms that packages will be installed locally in the environment, not globally.

### Deactivate the Environment
```bash
deactivate
```

---

## 5. Dependency Management

All Python packages for Month 1 will be defined in `python/requirements.txt`.

### Install All Dependencies
After activating the virtual environment:
```bash
pip install -r requirements.txt
```

### Install a New Package
```bash
pip install package_name
pip freeze > requirements.txt
```

---

## 6. Recommended Packages & Tools

### Core Python & APIs (Week 3)
* `requests`: For making web API HTTP requests.
* `ruff`: A fast Python linter and formatter.
* `pytest`: A clean framework for writing unit tests.

To install these, run:
```bash
pip install requests ruff pytest
```

### Data Science & AI/ML (Week 4)
* `numpy`: Array and matrix operations.
* `pandas`: Tabular data frames and manipulation.
* `matplotlib` & `seaborn`: Data visualization.
* `scikit-learn`: Simple and efficient machine learning models.
* `notebook`: Jupyter Notebooks interface.

To install these, run:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn notebook
```

---

## 7. Daily Run Command

To run a Python file:
```bash
python main.py
```
*(Ensure the virtual environment is active if the script uses external packages)*
