import math

biggest_number = -math.inf

current_data = input()

while current_data != 'Stop':
    current_data = int(current_data)
    if current_data > biggest_number:
        biggest_number = current_data
    current_data = input()

print(biggest_number)
