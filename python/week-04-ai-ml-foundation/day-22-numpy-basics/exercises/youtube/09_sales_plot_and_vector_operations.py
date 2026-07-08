# Sales Plot and Vector Operations
# Practice: Plot average cumulative sales and perform basic vector operations.

import matplotlib.pyplot as plt
import numpy as np


# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000],
    [3, 200000, 230000, 260000, 300000],
    [4, 180000, 210000, 240000, 270000],
    [5, 160000, 185000, 205000, 230000],
])

years = np.array([2021, 2022, 2023, 2024])
sales_without_id = sales_data[:, 1:]
cumulative_sales = np.cumsum(sales_without_id, axis=1)

# Graph size.
plt.figure(figsize=(10, 5))

# Plot average cumulative sales across all restaurants.
plt.plot(years, np.mean(cumulative_sales, axis=0), marker="o")

# Graph title and axis labels.
plt.title("Average Cumulative Sales Across All Restaurants")
plt.xlabel("Year")
plt.ylabel("Sales")

# Show grid and render graph.
plt.grid(True)
plt.show()


# Vector operations
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

print("Vector addition:", vector1 + vector2)
print("Vector subtraction:", vector1 - vector2)
print("Vector multiplication:", vector1 * vector2)
print("Vector division:", vector1 / vector2)
print("Dot product:", np.dot(vector1, vector2))
