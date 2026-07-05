# classes, constructors, objects, and instance attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

first_car = Car("Toyota", "Corolla")
second_car = Car("Tata", "Safari")

print("\n--- First Car ---")
print(f"Brand: {first_car.brand}")
print(f"Model: {first_car.model}")

print("\n--- Second Car ---")
print(f"Brand: {second_car.brand}")
print(f"Model: {second_car.model}")
