import math

class Figure:
    def __init__(self):
        self.area=0
        self.perimeter=0
    
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Square(Figure):
    def __init__(self,side=1):
        super().__init__()
        self.side=side

    def calculate_area(self):
        self.area = self.side * self.side

    def calculate_perimeter(self):
        self.perimeter = 4 * self.side

class Circle(Figure):
    def __init__(self, radius=1):
        super().__init__()
        self.radius = radius
    
    def calculate_area(self):
        self.area = math.pi * (self.radius**2)
    
    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius

class Triangle(Figure):
    def __init__(self, side=1):
        super().__init__()
        self.side = side
    
    def calculate_area(self):
        height= (math.sqrt(3)/2)* self.side
        self.area = (height * self.side) / 2
    
    def calculate_perimeter(self):
        self.perimeter = 3 * self.side

if __name__ == "__main__":

    square= Square(5)
    square.calculate_area()
    square.calculate_perimeter()
    print(f"The square area is {square.area} cm and the perimeter is {square.perimeter} cm.")

    circle = Circle(3)
    circle.calculate_area()
    circle.calculate_perimeter()
    print(f"The circle area is {circle.area} cm and the perimeter is {circle.perimeter} cm.")

    triangle = Triangle(2)
    triangle.calculate_area()
    triangle.calculate_perimeter()
    print(f"The triangle area is {triangle.area} cm and the perimeter is {triangle.perimeter} cm.")



       

