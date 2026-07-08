# Marks Filtering and Cleanup
# Practice boolean masks and np.where() to clean invalid values.

import numpy as np


print("\n==============================================")
print("          MARKS FILTERING AND CLEANUP          ")
print("==============================================\n")

# Some marks are invalid because they are below 0 or above 100.
raw_marks = np.array([78, 105, 88, -4, 67, 92, 101, 55])

print("Raw marks:", raw_marks)

valid_mask = (raw_marks >= 0) & (raw_marks <= 100)
invalid_mask = ~valid_mask

valid_marks = raw_marks[valid_mask]
invalid_marks = raw_marks[invalid_mask]

print("Valid marks:", valid_marks)
print("Invalid marks:", invalid_marks)

# Replace invalid marks with 0 so calculations can continue safely.
clean_marks = np.where(valid_mask, raw_marks, 0)

print("Clean marks:", clean_marks)
print("Total from clean marks:", np.sum(clean_marks))
print("Average from valid marks only:", np.mean(valid_marks))

result_labels = np.where(clean_marks >= 60, "Pass", "Fail")
print("Result labels after cleanup:", result_labels)
