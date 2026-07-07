# Encapsulation
# Problem: Modify the Truck class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Truck:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"


new_truck = Truck("Ford", "F150")
print(new_truck.get_brand())
print(new_truck.full_name())


# Property Decorators
# Problem: Use a property decorator in the Truck class to make the model attribute read-only

class ReadOnlyTruck:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    @property
    def model(self):
        return self.__model


new_read_only_truck = ReadOnlyTruck("Ford", "F150")
# new_read_only_truck.model = "City" # raises AttributeError because model is read-only
print(new_read_only_truck.model)

