import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle radius is {self.radius}. Circle area is {self.area():.2f}."

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


circle1 = Circle(3)
circle2 = Circle(20)

print("Circle1:", circle1)
print("Circle2:", circle2)
circle3 = circle1 + circle2
print("Added circles (circle1 + circle2:", circle3)

print("Is circle2 bigger than circle1:", circle2 > circle1)
print("Are circle1 and circle3 equal:", circle1 == circle3)

circles = [circle2, circle1, circle3]

for circle in circles:
    print("Unsorted:", circle)

circles.sort()

for circle in circles:
    print("Sorted:", circle)