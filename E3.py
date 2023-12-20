import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def invert_coordinates(self):
        self._x, self._y = self._y, self._x

    def __str__(self):
        return "({}, {})".format(self._x, self._y)

    def distance_to(self, other_point):
        return math.sqrt((self._x - other_point.x) ** 2 + (self._y - other_point.y) ** 2)


class Rectangle:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2

    @property
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, value):
        self._point1 = value

    @property
    def point2(self):
        return self._point2

    @point2.setter
    def point2(self, value):
        self._point2 = value

    @property
    def area(self):
        width = abs(self._point1.x - self._point2.x)
        height = abs(self._point1.y - self._point2.y)
        return width * height

    @property
    def perimeter(self):
        width = abs(self._point1.x - self._point2.x)
        height = abs(self._point1.y - self._point2.y)
        return 2 * (width + height)

# Programa de prueba
p1 = Point(1, 1)
p2 = Point(3, 3)
r = Rectangle(p1, p2)
print("Area:", r.area) # Output: 4
print("Perimeter:", r.perimeter) # Output: 8
