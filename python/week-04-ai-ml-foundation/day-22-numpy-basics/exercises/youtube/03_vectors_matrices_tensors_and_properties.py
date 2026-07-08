# Vectors, Matrices, Tensors, and Array Properties
# Practice: Understand NumPy dimensions and inspect shape, ndim, size, and dtype.

import numpy as np


# A 1D array is commonly called a vector.
vector = np.array([1, 2, 3])
print("Vector:\n", vector)

# A 2D array is commonly called a matrix.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatrix:\n", matrix)

# An array with more than 2 dimensions is commonly called a tensor.
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nTensor:\n", tensor)


# Array properties
arr = np.array([[1, 2, 3], [4, 5, 6]])  # dtype: int64 on many systems

# dtype examples:
# np.array([[1, 2, 3], [4, 5, True]])    -> usually int64 because True becomes 1
# np.array([[1, 2, 3], [4, 5, 6.8]])     -> float64 because one value is a float
# np.array([[1, 2, 3], [4, 5, "6.8"]])   -> string dtype because one value is text

print("\nShape:", arr.shape)      # rows and columns: (2, 3)
print("Dimension:", arr.ndim)     # number of dimensions
print("Size:", arr.size)          # total number of elements
print("DType:", arr.dtype)        # data type of the array elements
