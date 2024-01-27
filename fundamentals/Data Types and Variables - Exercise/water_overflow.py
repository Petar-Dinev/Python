num_of_lines = int(input())
capacity_of_water_tank = 255
water_in_water_tank = 0

for i in range(num_of_lines):
    current_liters_of_water = int(input())

    if water_in_water_tank + current_liters_of_water <= capacity_of_water_tank:
        water_in_water_tank += current_liters_of_water
    else:
        print('Insufficient capacity!')

print(water_in_water_tank)
