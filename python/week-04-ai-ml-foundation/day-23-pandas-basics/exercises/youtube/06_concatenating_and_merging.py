# Crash-course practice: combine DataFrames with concat and merge.

import pandas as pd


class_a = pd.DataFrame(
    {
        "name": ["Harry", "Rohan", "Shubham"],
        "marks": [100, 53, 45],
        "city": ["Delhi", "Mumbai", "Delhi"],
    }
)
class_b = pd.DataFrame(
    {
        "name": ["Kashif", "Thamizh", "Ken"],
        "marks": [53, 70, 90],
        "city": ["Kolkata", "Chennai", "Mumbai"],
    }
)

# concat stacks tables that share the same columns. ignore_index=True creates a
# fresh index instead of preserving both tables' 0, 1, 2 indexes.
all_students = pd.concat([class_a, class_b], ignore_index=True)
print("All students after concat:\n", all_students)

attendance = pd.DataFrame(
    {
        "name": ["Kashif", "Thamizh", "Ken", "Akarsh"],
        "attendance_percentage": [92, 88, 95, 81],
    }
)

# merge combines related columns using a shared key. 
# The on parameter tells Pandas which column to use as the matching link between the two tables.
result = pd.merge(class_b, attendance, on="name")
print("\nMerge result:\n", result)

