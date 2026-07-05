# self and instance methods.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def description(self):
        return f"This car is a {self.full_name()}."


car = Car("Suzuki", "Jimny")

print(car.full_name())
print(car.description())
