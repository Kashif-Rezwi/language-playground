# Array Reshaping
# Practice: Reshape arrays, flatten arrays, use ravel, and transpose dimensions.

import numpy as np


# Create an array from 0 to 11. This gives 12 items.
arr = np.arange(12)
print("\nOriginal array:\n", arr)

# Reshape the flat/1D array into 3 rows and 4 columns.
# The new shape must use the same total number of elements.
reshaped_arr = arr.reshape(3, 4)
print("\nReshaped array:\n", reshaped_arr)

# flatten() returns a new 1D copy of the array.
flattened_arr = reshaped_arr.flatten()
print("\nFlattened array:\n", flattened_arr)

# ravel() returns a 1D view when possible, so changes may affect the original array.
raveled = reshaped_arr.ravel()
print("\nRaveled array:\n", raveled)

# Transpose flips the array dimensions: rows become columns and columns become rows.
transposed = reshaped_arr.T
# transposed = reshaped_arr.transpose()  # same result as .T
print("\nTransposed array:\n", transposed)
