# Practice name mangling and read-only properties.

class Truck:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    def full_name(self):
        return f"{self.brand} {self.model}"


truck = Truck("Ford", "F-150")

print(f"Brand: {truck.brand}")
print(f"Model: {truck.model}")
print(f"Full name: {truck.full_name()}")

# No property setter exists, so this would raise AttributeError:
# truck.model = "Ranger"
