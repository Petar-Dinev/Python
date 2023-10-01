length = float(input())
width = float(input())

length_in_centimeters = length * 100
width_in_centimeters = width * 100 - 100

nums_of_desks_in_length = length_in_centimeters // 120
nums_of_desks_in_width = width_in_centimeters // 70

total_desks = nums_of_desks_in_length * nums_of_desks_in_width
total_desks_without_door_and_department = total_desks - 3
print(total_desks_without_door_and_department)
