import math


def find_distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    distance = math.sqrt(a ** 2 + b ** 2)
    return distance


def find_closer_point(p1_x, p1_y, p2_x, p2_y):
    p1_distance = find_distance(p1_x, p1_y, 0, 0)
    p2_distance = find_distance(p2_x, p2_y, 0, 0)

    if p1_distance > p2_distance:
        return f"({math.floor(p2_x)}, {math.floor(p2_y)})"
    else:
        return f"({math.floor(p1_x)}, {math.floor(p1_y)})"


point1_x = float(input())
point1_y = float(input())
point2_x = float(input())
point2_y = float(input())

print(find_closer_point(point1_x, point1_y, point2_x, point2_y))
