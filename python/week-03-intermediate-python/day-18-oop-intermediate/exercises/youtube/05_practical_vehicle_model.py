# Combine Day 18 concepts in a small practical vehicle model.

class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Vehicle.total_vehicles += 1

    def fuel_type(self):
        return "Petrol / Diesel"

    def description(self):
        return f"{self.brand} {self.model}"


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electric"

    def description(self):
        return f"{super().description()} ({self.battery_capacity})"


vehicle = Vehicle("Toyota", "Corolla")
electric_vehicle = ElectricVehicle("Tata", "Nexon EV", "40.5 kWh")

print(f"{vehicle.description()} - {vehicle.fuel_type()}")
print(f"{electric_vehicle.description()} - {electric_vehicle.fuel_type()}")

print(f"Total vehicles: {Vehicle.total_vehicles}")
