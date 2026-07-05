# Optional preview of multiple inheritance with stateless mixins.

class BatteryInfoMixin:
    def battery_info(self):
        return "Battery system available"


class EngineInfoMixin:
    def engine_info(self):
        return "Electric motor available"


class Jet:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricJet(BatteryInfoMixin, EngineInfoMixin, Jet):
    pass


electric_jet = ElectricJet("Eviation", "Alice")

print(electric_jet.full_name())
print(electric_jet.battery_info())
print(electric_jet.engine_info())
