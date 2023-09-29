height_on_house = float(input())
side_wall_length = float(input())
height_triangle_side_on_roof = float(input())

area_of_front_and_back_wall = height_on_house ** 2 * 2 - 2 * 1.2
area_of_side_walls = 2 * (height_on_house * side_wall_length) - 2 * (1.5 ** 2)
green_paint_litres = (area_of_side_walls + area_of_front_and_back_wall) / 3.4

area_of_roof = 2 * (height_on_house * side_wall_length) + 2 * (height_on_house * height_triangle_side_on_roof / 2)
red_paint_litres = area_of_roof / 4.3
print(f"{green_paint_litres:.2f}")
print(f"{red_paint_litres:.2f}")
