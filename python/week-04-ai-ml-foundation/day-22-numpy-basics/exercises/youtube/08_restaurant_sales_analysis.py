# Practice With Real-World Data
# Practice: Analyze restaurant sales data with NumPy aggregations.

import numpy as np


# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000],  # Chai Point
])

print("=" * 12 + " Zomato Sales Analysis " + "=" * 12)

# Find the shape of the data.
print("\nSales data shape:", sales_data.shape)

# Find first 3 restaurant rows.
print("\nFirst 3 restaurant rows:\n", sales_data[0:3])

# Find last 3 restaurant rows.
print("\nLast 3 restaurant rows:\n", sales_data[-3:])

# Find all restaurant sales data excluding the id column.
# ":" means all rows.
# "1:" means columns from index 1 to the end.
sales_without_id = sales_data[:, 1:]
print("\nSales data without restaurant id:\n", sales_without_id)


# Total sales per year.
yearly_sales_with_id = np.sum(sales_data, axis=0)
print("\nTotal per column including restaurant ids:", yearly_sales_with_id)

yearly_sales_without_id = np.sum(sales_without_id, axis=0)
print("Total sales per year:", yearly_sales_without_id)


# Minimum and maximum sales per restaurant.
min_sales_per_restaurant = np.min(sales_without_id, axis=1)
print("\nMinimum sales per restaurant:", min_sales_per_restaurant)

max_sales_per_restaurant = np.max(sales_without_id, axis=1)
print("Maximum sales per restaurant:", max_sales_per_restaurant)


# Minimum and maximum sales per year.
min_sales_per_year = np.min(sales_without_id, axis=0)
print("\nMinimum sales per year:", min_sales_per_year)

max_sales_per_year = np.max(sales_without_id, axis=0)
print("Maximum sales per year:", max_sales_per_year)


# Average sales per restaurant and per year.
avg_sales_per_restaurant = np.mean(sales_without_id, axis=1)
print("\nAverage sales per restaurant:", avg_sales_per_restaurant)

avg_sales_per_year = np.mean(sales_without_id, axis=0)
print("Average sales per year:", avg_sales_per_year)


# Broadcasting: 12 is applied to every sales value.
monthly_avg_sales = sales_without_id / 12
print("\nAverage sales per month:\n", monthly_avg_sales)


# Cumulative sales for each restaurant across years.
cumulative_sales = np.cumsum(sales_without_id, axis=1)
print("\nCumulative sales:\n", cumulative_sales)
