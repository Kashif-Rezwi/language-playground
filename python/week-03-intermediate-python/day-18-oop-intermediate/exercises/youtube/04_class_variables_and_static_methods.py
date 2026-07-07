# Class Variables
# Problem: Add a class variable to Truck That keeps track of the numbers of cars created.

class Truck:
    total_trucks = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Truck.total_trucks += 1

    def full_name(self):
        return f"{self.brand} {self.model}"


new_truck = Truck("Ford", "F150")
print(new_truck.full_name())

new_truck2 = Truck("Toyota", "Camry")
print(new_truck2.full_name())

print(Truck.total_trucks)


# Static Method
# Problem: Add static method to the Truck class that returns a general description of a truck.

class StaticTruck:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def general_description():
        return "This is a truck"


new_static_truck = StaticTruck("Ford", "F150")
print(new_static_truck.general_description())
print(StaticTruck.general_description())