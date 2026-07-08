# Sales Matrix Analysis
# Practice totals, averages, masks, and argmax with a product sales matrix.

import numpy as np


print("\n==============================================")
print("            SALES MATRIX ANALYSIS             ")
print("==============================================\n")

product_names = np.array(["Laptop", "Phone", "Headphones", "Keyboard"])
month_names = np.array(["Jan", "Feb", "Mar", "Apr"])

# Rows are products. Columns are monthly sales.
sales = np.array([
    [52000, 61000, 58000, 72000],
    [45000, 48000, 53000, 59000],
    [12000, 15000, 17000, 16000],
    [9000, 11000, 10000, 13000],
])

print("Sales matrix:\n", sales)

product_totals = np.sum(sales, axis=1)
monthly_totals = np.sum(sales, axis=0)
product_monthly_averages = np.mean(sales, axis=1)

best_product_index = np.argmax(product_totals)
monthly_target = 130000
target_crossed = monthly_totals >= monthly_target

print("\n--- Product Summary ---")

for index, product_name in enumerate(product_names):
    print(
        f"{product_name}: total INR {product_totals[index]:,}, "
        f"monthly average INR {product_monthly_averages[index]:,.2f}"
    )

print("\n--- Monthly Summary ---")

for index, month_name in enumerate(month_names):
    print(f"{month_name}: total INR {monthly_totals[index]:,}")

print(
    "\nBest product by total sales:",
    product_names[best_product_index],
)
print("Months crossing target:", month_names[target_crossed])
