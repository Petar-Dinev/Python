import math

radius = float(input())

area_of_circle = (radius * radius) * math.pi
perimeter_of_circle = (radius + radius) * math.pi

print(f"{area_of_circle:.2f}")
print(f"{perimeter_of_circle:.2f}")

