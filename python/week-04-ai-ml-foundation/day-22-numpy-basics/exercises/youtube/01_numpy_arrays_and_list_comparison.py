# NumPy Foundation
# Practice: Create basic NumPy arrays and compare list multiplication with NumPy array multiplication.

import numpy as np


arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("1D array:", arr_1d)

# Incorrect:
# arr_2d = np.array([1, 2, 3], [4, 5, 6])
#
# np.array expects one main object as input. For a 2D array, pass a nested list.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:", arr_2d)


# List vs NumPy array
# Python list multiplication repeats the list.
py_list = [1, 2, 3]
print("Python list multiplication:", py_list * 3)

# NumPy array multiplication performs element-wise multiplication.
np_array = np.array([1, 2, 3])
print("NumPy array multiplication:", np_array * 3)
