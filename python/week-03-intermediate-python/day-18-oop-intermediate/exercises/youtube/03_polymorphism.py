# Polymorphism
# Problem: Demonstrate a polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class SuperCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricSuperCar(SuperCar):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electric"


new_super_car = SuperCar("ferrari", "spider")
print(f"{new_super_car.model} {new_super_car.fuel_type()}")

new_electric_super_car = ElectricSuperCar("Tesla", "Model S")
print(f"{new_electric_super_car.model} {new_electric_super_car.fuel_type()}")

