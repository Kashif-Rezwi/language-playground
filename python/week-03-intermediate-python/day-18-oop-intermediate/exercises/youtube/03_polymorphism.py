# Practice polymorphism through method overriding.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or diesel"


class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"


def print_fuel_details(vehicle):
    print(f"{vehicle.brand} {vehicle.model}: {vehicle.fuel_type()}")


petrol_car = Car("Ferrari", "Spider")
electric_car = ElectricCar("Tesla", "Model S")

print_fuel_details(petrol_car)
print_fuel_details(electric_car)
