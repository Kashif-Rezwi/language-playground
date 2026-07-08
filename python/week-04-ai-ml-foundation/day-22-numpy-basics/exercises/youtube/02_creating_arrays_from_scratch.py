# Creating Arrays From Scratch
# Practice: Create arrays using zeros, ones, full, random, arange, and linspace.

import numpy as np


# Create a 3 x 4 array filled with zeros.
zeros = np.zeros((3, 4))
print("\nZeros array:\n", zeros)

# Create a 2 x 3 array filled with ones.
ones = np.ones((2, 3))
print("\nOnes array:\n", ones)

# Create a 2 x 2 array filled with a constant value.
full = np.full((2, 2), 7)
print("\nFull array:\n", full)

# Create an array using random values between 0 and 1.
random_values = np.random.random((2, 3))
print("\nRandom array:\n", random_values)

# Create a sequence using arange(start, stop, step).
# 0 to 10 is the range, and 2 is the step size. The stop value is excluded.
sequence = np.arange(0, 10, 2)
print("\nSequence array:\n", sequence)

# Create evenly spaced values using linspace(start, stop, number_of_values).
# Here 0 to 10 is split into 5 equal points, and the stop value is included.
linspace_values = np.linspace(0, 10, 5)
print("\nLinspace array:\n", linspace_values)
