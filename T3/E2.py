# Create a class to represent a car. The class should have the following attributes: make, model, colour, number of doors, and engine power. It should also have the following methods:
# • Constructor: initializes the attributes with default values.
# • Getters and setters: to access and modify the attributes.
# • Method to print the car's information.

import math

class Car:
    def __init__(self, make, model, colour, num_doors, engine_power):
        self.make = make
        self.model = model
        self.colour = colour
        self.num_doors = num_doors
        self.engine_power = float(engine_power)

    def get_make(self):
        return self.make
    def set_make(self,make):
        self.make = make

    def get_model(self):
        return self.model
    def set_model(self,model):
        self.model=model
    
    def get_colour(self):
        return self.colour
    def set_colour(self,colour):
        self.colour = colour

    def get_num_doors(self):
        return self.num_doors
    def set_num_doors(self,num_doors):
        self.num_doors = num_doors

    def get_engine_power(self):
        return self.engine_power
    def set_engine_power(self,engine_power):
        self.engine_power = engine_power

    def __str__(self):
        return f"Car's make: {self.make}, model: {self.model}, colour: {self.colour}, number of doors: {self.num_doors} and engine power: {self. engine_power}."
    
    def print_info(self):
        print("Car Information:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Number of doors: {self.num_doors}")
        print(f"Engine Power: {self.engine_power}")


    
car= Car("Ford", "Fiesta", "Red", 5, 140.6 )
print(car)

car.print_info()