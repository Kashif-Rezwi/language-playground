# Operations on NumPy Arrays
# Practice: Use slicing, negative indexing, 2D indexing, sorting, filtering, and masks.

import numpy as np


# Basic slicing on a 1D array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Basic slicing:", arr[2:7])       # indexes 2 to 6
print("Slicing with step:", arr[2:7:2]) # indexes 2 to 6, moving by 2
print("Negative indexing:", arr[-1])    # last item
print("Negative indexing:", arr[-3])    # third item from the end


# Operations on a multi-dimensional array.
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nSingle item:", arr_2d[1, 2])   # row index 1, column index 2
print("Entire row:", arr_2d[1])         # row at index 1
print("Entire column:", arr_2d[:, 1])   # all rows, column at index 1


# Sorting a 1D array.
unsorted = np.array([2, 3, 5, 1, 4, 8, 10, 7, 6, 9])
print("\nUnsorted array:\n", unsorted)
print("\nSorted array:\n", np.sort(unsorted))

# Sorting a 2D array.
arr_2d_unsorted = np.array([[3, 1], [1, 2], [2, 3]])
print("\nUnsorted 2D array:\n", arr_2d_unsorted)
print("\nSorted 2D array by row:\n", np.sort(arr_2d_unsorted, axis=1))
print("\nSorted 2D array by column:\n", np.sort(arr_2d_unsorted, axis=0))


# Filtering with boolean expressions.
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

even_numbers = numbers[numbers % 2 == 0]
print("\nEven numbers:\n", even_numbers)

odd_numbers = numbers[numbers % 2 != 0]
print("\nOdd numbers:\n", odd_numbers)

# A mask is a boolean array used inside [] to filter values.
mask = numbers > 5
print("Numbers greater than 5:", numbers[mask])
