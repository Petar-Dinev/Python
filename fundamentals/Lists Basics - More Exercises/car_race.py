time_list = [int(number) for number in input().split()]
left_car_time = 0
right_car_time = 0

finish_index = len(time_list) // 2

for i in range(finish_index):
    current_left_car_time = time_list[i]
    if current_left_car_time == 0:
        left_car_time *= 0.8
    else:
        left_car_time += current_left_car_time

    current_right_car_time = time_list[i * -1 - 1]
    if current_right_car_time == 0:
        right_car_time *= 0.8
    else:
        right_car_time += current_right_car_time

winner = 'left' if left_car_time < right_car_time else 'right'
winner_time = left_car_time if left_car_time < right_car_time else right_car_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
