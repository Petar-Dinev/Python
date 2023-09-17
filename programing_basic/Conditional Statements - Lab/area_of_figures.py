import math
figure = input()
result = 0
if figure == 'square':
    side_of_square = float(input())
    result = side_of_square * side_of_square
elif figure == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif figure == 'circle':
    radius = float(input())
    result = math.pi * radius * radius
else:
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f"{result:.3f}")
