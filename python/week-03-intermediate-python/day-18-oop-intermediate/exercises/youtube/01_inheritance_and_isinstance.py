# Practice single inheritance, super(), and isinstance()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
        

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


electric_car = ElectricCar("Tesla", "Model S", "100 kWh")

print(electric_car.full_name())
print(f"Battery: {electric_car.battery_capacity}")
print(f"Is a Car: {isinstance(electric_car, Car)}")
print(f"Is an ElectricCar: {isinstance(electric_car, ElectricCar)}")
