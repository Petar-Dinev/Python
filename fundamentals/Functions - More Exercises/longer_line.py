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
        return f"({math.floor(p2_x)}, {math.floor(p2_y)})({math.floor(p1_x)}, {math.floor(p1_y)})"
    else:
        return f"({math.floor(p1_x)}, {math.floor(p1_y)})({math.floor(p2_x)}, {math.floor(p2_y)})"


first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())
third_point_x = float(input())
third_point_y = float(input())
fourth_point_x = float(input())
fourth_point_y = float(input())

first_line_distance = find_distance(first_point_x, first_point_y, second_point_x, second_point_y)
second_line_distance = find_distance(third_point_x, third_point_y, fourth_point_x, fourth_point_y)

if first_line_distance >= second_line_distance:
    print(find_closer_point(first_point_x, first_point_y, second_point_x, second_point_y))
else:
    print(find_closer_point(third_point_x, third_point_y, fourth_point_x, fourth_point_y))
