# Day 18: Classes in Practical Projects
# Topic: record modelling, validation, state changes, and __str__

class InventoryItem:

    def __init__(self, name, category, price, quantity):
        self.name = " ".join(name.split()).title()
        self.category = " ".join(category.split()).title()
        self.price = price
        self.quantity = quantity

    def details_are_valid(self):
        # return whether the item has a usable starting state.
        return (
            self.name != ""
            and self.category != ""
            and self.price >= 0
            and self.quantity >= 0
        )

    def calculate_stock_value(self):
        # return the total value of all currently available units.
        return self.price * self.quantity
    
    def is_in_stock(self):
        # return true when at least one unit is available.
        return self.quantity > 0

    def restock(self, amount):
        # add a positive quantity and report whether it succeeded.
        if amount <= 0:
            return False
        self.quantity = self.quantity + amount
        return True

    def sell(self, amount):
        # remove available units without allowing negative stock.
        if amount <= 0 or amount > self.quantity:
            return False
        self.quantity = self.quantity - amount
        return True
        
    # __str__ is a built-in special method that tells Python how to represent your object as a readable string.
    def __str__(self):
        # return a short, readable description for print(item)
        stock_status = "In Stock" if self.is_in_stock() else "Out of Stock"

        return (
            f"{self.name} ({self.category}) | "
            f"₹{self.price:.2f} | {self.quantity} units | "
            f"{stock_status}"
        )
        
        
print("\n==============================================")
print("          Practical Inventory Model           ")
print("==============================================\n")

# Create two independent records from the same class.
keyboard = InventoryItem(
    "  mechanical   keyboard  ",
    "computer accessories",
    2499,
    8,
)
mouse = InventoryItem(
    "wireless mouse",
    "computer accessories",
    899,
    15,
)


print("--- Initial Inventory ---")
print(keyboard)
print(mouse)

print("\n--- Calculated Values ---")
print(f"{keyboard.name} stock value: INR {keyboard.calculate_stock_value():,.2f}")
print(f"{mouse.name} stock value: INR {mouse.calculate_stock_value():,.2f}")

# sell operation: a successful command method changes only the selected object.
print("\n--- Sell 2 Keyboards ---")

if keyboard.sell(2):
    print("Sale completed.")
else:
    print("Sale failed. Check the requested quantity.")

print(keyboard)
print(mouse)


# sell operarion: The class rejects a sale that would make quantity negative.
print("\n--- Attempt to Sell 20 Keyboards ---")

if keyboard.sell(20):
    print("Sale completed.")
else:
    print("Sale failed. Not enough stock.")

print(keyboard)


# restocking operation: Restocking updates the object's state through a method.
print("\n--- Restock Keyboards ---")

if keyboard.restock(10):
    print("Restock completed.")
else:
    print("Restock failed. Enter a positive quantity.")

print(keyboard)


# validation: Invalid starting data can be detected before using the record.
invalid_item = InventoryItem("", "accessories", -500, -2)

print("\n--- Validation Check ---")
print(f"Keyboard details valid: {keyboard.details_are_valid()}")
print(f"Invalid item details valid: {invalid_item.details_are_valid()}")


# __str__ returns text, so it also works inside an f-string.
print("\n--- Readable Object Output ---")
print(f"Keyboard inventory item: {keyboard}")
print(f"Mouse inventory item: {mouse}")