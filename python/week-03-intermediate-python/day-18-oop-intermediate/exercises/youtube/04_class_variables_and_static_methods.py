# Practice class variables and static methods.

class Truck:
    total_trucks = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Truck.total_trucks += 1

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def general_description():
        return "A truck is a vehicle designed to carry or tow loads."



first_truck = Truck("Ford", "F-150")
second_truck = Truck("Toyota", "Tacoma")

print(first_truck.full_name())
print(second_truck.full_name())
print(f"Trucks created: {Truck.total_trucks}")
print(Truck.general_description())