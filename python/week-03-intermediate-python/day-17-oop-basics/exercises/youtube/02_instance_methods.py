# Class Method and Self (Note: This is an Instance Method)
# Problem: Add a method to the Car class that displays the full name of the car (brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


new_car = Car("Suzuki", "Jipsy")
print(new_car.full_name())

