import math

lowest_number = math.inf

current_data = input()

while current_data != 'Stop':
    current_data = int(current_data)
    if current_data < lowest_number:
        lowest_number = current_data
    current_data = input()

print(lowest_number)
