# -*- coding: utf-8 -*-
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.fuel_level = 100  # Initial fuel level

    def drive(self, distance):
        fuel_needed = distance / 10  # 1 unit of fuel for every 10 km
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            print(f"Drove {distance} km. Fuel level is now {self.fuel_level}.")
        else:
            print("Insufficient fuel to drive the distance specified.")

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"Refueled {amount} units. Fuel level is now {self.fuel_level}.")

    def display_status(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Fuel Level: {self.fuel_level}")

# Example usage:
car1 = Car("Toyota", "Corolla")
car1.display_status()
car1.drive(50)  # Should reduce fuel level
car1.display_status()
car1.refuel(20)  # Should increase fuel level
car1.display_status()


    