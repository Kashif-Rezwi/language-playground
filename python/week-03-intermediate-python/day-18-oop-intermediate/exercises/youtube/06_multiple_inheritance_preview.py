# Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance. (Note: The implementation uses ElectricJet inheriting from Battery, Engine, and Jet).

class Jet:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class Battery:
    def battery_info(self):
        return "This is a battery"


class Engine:
    def engine_info(self):
        return "This is an engine"


class ElectricJet(Battery, Engine, Jet):
    pass


my_electric_jet = ElectricJet("Tesla", "Dragon S")

print(my_electric_jet.full_name())
print(my_electric_jet.battery_info())
print(my_electric_jet.engine_info())

