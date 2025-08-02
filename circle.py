import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * self.radius ** 2
    
    def cal_diameter(self):
        return 2 * self.radius

def main():
    c1 = Circle(14)
    print(c1.radius)
    area = c1.calc_area()
    print(f"{area:.3f}")

    diameter = c1.cal_diameter()
    print(f"{diameter:.3f}")

if __name__ == "__main__":
    main()
