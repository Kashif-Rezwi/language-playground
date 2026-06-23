# Python Setup Guide

This file contains the basic setup commands and workflow for Python learning inside this repository.

## Check Python Version

```bash
python --version
```

or:

```bash
python3 --version
```

## Create a Virtual Environment

From the `python` directory:

```bash
python -m venv .venv
```

or:

```bash
python3 -m venv .venv
```

## Activate Virtual Environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## Deactivate Virtual Environment

```bash
deactivate
```

## Install a Package

Example:

```bash
pip install requests
```

## Save Dependencies

```bash
pip freeze > requirements.txt
```

## Install Dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

## Recommended Python Learning Packages

For core Python:

```bash
pip install requests
```

For data analysis and AI/ML foundation:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Daily Run Command

To run a Python file:

```bash
python exercises.py
```

or:

```bash
python main.py
```

## Important Rule

Use a virtual environment when working with external packages.
