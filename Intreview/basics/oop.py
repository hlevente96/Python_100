class Circle:
    def __init__(self, radius):
        self._radius = radius  # private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

# Example usage:
c = Circle(5)
print(c.radius)  # Accessing the radius like an attribute
print(c.area)    # Accessing the area like an attribute

c.radius = 10  # Set the radius using the setter
print(c.area)  # The area will be recalculated based on the new radius






class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(10, 5)
print(r.area)  # Access area like an attribute
r.width = 15    # Modify width like an attribute
print(r.area)





class Car:
    wheels = 4  # Class attribute

    def __init__(self, model, year):
        self.model = model
        self.year = year

    @classmethod
    def create_sports_car(cls, model):
        return cls(model, 2025)  # Create a Car with a default year of 2025

    @classmethod
    def display_wheels(cls):
        print(f"A car has {cls.wheels} wheels.")

# Usage:
sports_car = Car.create_sports_car("Ferrari")
print(sports_car.model)  # Output: Ferrari
print(sports_car.year)   # Output: 2025
Car.display_wheels()     # Output: A car has 4 wheels.


