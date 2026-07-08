# Fancy Indexing, np.where, and Combining Arrays
# Practice: Select values by index, use np.where, add arrays, and concatenate arrays.

import numpy as np


numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
indices = [0, 2, 4]

# Fancy indexing selects specific positions from the array.
print("Extracting items using indexing:", numbers[indices])

# np.where(condition) returns the indexes where the condition is True.
where_result = np.where(numbers > 5)
print("Extracting items using np.where():", numbers[where_result])

# np.where(condition, x, y) chooses from x where True and y where False.
# condition: numbers > 5
# x: numbers * 2, used when the condition is True
# y: numbers, used when the condition is False
condition_array = np.where(numbers > 5, numbers * 2, numbers)
print("Condition array:", condition_array)

# Another simple np.where example that returns labels instead of numbers.
condition_labels = np.where(numbers > 5, "true", "false")
print("Condition labels:", condition_labels)


# Adding, removing, and merging data.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition: [1 + 4, 2 + 5, 3 + 6] = [5, 7, 9]
combined_by_addition = arr1 + arr2
print("Combined by addition:", combined_by_addition)

# Concatenation joins arrays end to end: [1, 2, 3, 4, 5, 6]
combined_by_concatenate = np.concatenate((arr1, arr2))
print("Combined by concatenate:", combined_by_concatenate)
