# Define a base class for all vehicles
class Vehicle:
    def __init__(self, name: str, mpg: float):
        # Store the name of the vehicle and its miles per gallon
        self.name = name
        self.mpg = mpg

    def fuel_needed(self, distance: float) -> float:
        # Calculate how much fuel is needed for a given distance
        return distance / self.mpg

    def description(self) -> str:
        # Return a simple message about mpg
        return f"{self.name} gets {self.mpg} miles per gallon."


# Subclasses that use the Vehicle superclass
class Car(Vehicle):
    def __init__(self):
        super().__init__("Car", 30)


class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", 50)


class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)

if __name__ == "__main__":
    car = Car()
    truck = Truck()
    bus = Bus()
    motorcycle = Motorcycle()

    print(car.description())
    print("Fuel needed for 120 miles:", car.fuel_needed(120))  # Expected: 4.0

    print(truck.description())
    print("Fuel needed for 150 miles:", truck.fuel_needed(150))  # Expected: 10.0

    print(bus.description())
    print("Fuel needed for 80 miles:", bus.fuel_needed(80))  # Expected: 10.0

    print(motorcycle.description())
    print("Fuel needed for 100 miles:", motorcycle.fuel_needed(100))  # Expected: 2.0

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 