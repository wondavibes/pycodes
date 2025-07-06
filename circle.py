import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * self.radius ** 2



c1 = circle(14)
print(c1.radius)
area = c1.calc_area()
print(f"{area:.3f}")
