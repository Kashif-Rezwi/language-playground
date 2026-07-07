# Product Record
# Models product data, calculates a discount, and uses readable object output.


class Product:
    def __init__(self, name, category, price, discount_percentage=0):
        self.name = " ".join(name.split()).title()
        self.category = " ".join(category.split()).title()
        self.price = price
        self.discount_percentage = discount_percentage

    def discount_is_valid(self):
        return 0 <= self.discount_percentage <= 100

    def calculate_discounted_price(self):
        if not self.discount_is_valid():
            return self.price

        discount_amount = self.price * self.discount_percentage / 100
        return self.price - discount_amount

    def is_affordable(self, budget):
        return budget >= self.calculate_discounted_price()

    def __str__(self):
        discounted_price = self.calculate_discounted_price()
        return (
            f"{self.name} | {self.category} | "
            f"INR {discounted_price:,.2f} after "
            f"{self.discount_percentage:.0f}% discount"
        )


print("\n==========================================")
print("              PRODUCT RECORD              ")
print("==========================================\n")

laptop = Product("student laptop", "electronics", 65000, 10)
headphones = Product("wireless headphones", "electronics", 4500, 15)

for product in (laptop, headphones):
    print(product)
    print(f"Original price: INR {product.price:,.2f}")
    print(f"Affordable with INR 50,000: {product.is_affordable(50000)}")
    print()
