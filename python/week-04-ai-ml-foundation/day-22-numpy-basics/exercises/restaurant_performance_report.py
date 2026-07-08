# Restaurant Performance Report
# Mini-project: Analyze yearly restaurant sales with a 2D NumPy array.

import numpy as np


print("\n==============================================")
print("        RESTAURANT PERFORMANCE REPORT         ")
print("==============================================\n")

restaurant_names = np.array([
    "Paradise Biryani",
    "Beijing Bites",
    "Pizza Hub",
    "Burger Point",
    "Chai Point",
])
years = np.array([2021, 2022, 2023, 2024])

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000],
    [3, 200000, 230000, 260000, 300000],
    [4, 180000, 210000, 240000, 270000],
    [5, 160000, 185000, 205000, 230000],
])

restaurant_ids = sales_data[:, 0]
sales = sales_data[:, 1:]

print("Restaurant IDs:", restaurant_ids)
print("Sales matrix:\n", sales)

total_sales_per_restaurant = np.sum(sales, axis=1)
average_sales_per_year = np.mean(sales, axis=0)
best_restaurant_index = np.argmax(total_sales_per_restaurant)

# Difference between each year and the previous year.
year_over_year_growth = sales[:, 1:] - sales[:, :-1]

print("\n--- Restaurant Totals ---")

for index, restaurant_name in enumerate(restaurant_names):
    print(
        f"{restaurant_name}: "
        f"INR {total_sales_per_restaurant[index]:,}"
    )

print("\n--- Average Sales Per Year ---")

for index, year in enumerate(years):
    print(f"{year}: INR {average_sales_per_year[index]:,.2f}")

print(
    "\nBest restaurant:",
    restaurant_names[best_restaurant_index],
)

print("\n--- Year-over-Year Growth ---")

for index, restaurant_name in enumerate(restaurant_names):
    print(f"{restaurant_name}: {year_over_year_growth[index]}")
