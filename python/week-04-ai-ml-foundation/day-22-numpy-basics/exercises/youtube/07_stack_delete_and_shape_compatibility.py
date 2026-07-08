# Array Compatibility, Stacking, and Deleting
# Practice: Check compatible shapes, add rows/columns, and delete array values.

import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

print("Compatibility shape for a and b:", a.shape == b.shape)
print("Compatibility shape for a and c:", a.shape == c.shape)


original = np.array([[1, 2], [3, 4]])
new_row = np.array([5, 6])
new_column = np.array([[5], [6]])

# Add a new row to the original array.
with_new_row = np.vstack((original, new_row))

# Add a new column to the original array.
with_new_column = np.hstack((original, new_column))

print("\nOriginal:\n", original)
print("\nWith new row:\n", with_new_row)
print("\nWith new column:\n", with_new_column)


arr = np.array([1, 2, 3, 4, 5])

# np.delete returns a modified copy. It does not return the deleted item.
deleted = np.delete(arr, 2)  # 2 is the index to remove
print("\nDelete from array:", deleted)
