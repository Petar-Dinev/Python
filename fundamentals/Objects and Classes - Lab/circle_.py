class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle):
        return (self.radius ** 2) * angle / 360 * Circle.__pi


circle = Circle(10)
angle_ = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle_):.2f}")
