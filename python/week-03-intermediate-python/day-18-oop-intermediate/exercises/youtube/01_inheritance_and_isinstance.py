# Inheritence
# Problem: Create an ElectricCar class that inherits from the Car class and has an addidtional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)


new_electric_car = ElectricCar("Tesla", "Model S", "200KW")
print(new_electric_car.full_name())
print(new_electric_car.battery_size)


# Class Inheritance and Instance() function
# Problem: Demonstrate the use of isinstance to check if new_truck is a Truck and ElectricTruck.

class Truck:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        print(f"{self.brand} {self.model}")


class ElectricTruck(Truck):
    def __init__(self, brand, model):
        super().__init__(brand, model)


new_truck = Truck("Ford", "F150")
new_electric_truck = ElectricTruck("Tesla", "CyberTruck")

print(isinstance(new_truck, Truck))
print(isinstance(new_truck, ElectricTruck))
print(isinstance(new_electric_truck, Truck))
print(isinstance(new_electric_truck, ElectricTruck))

