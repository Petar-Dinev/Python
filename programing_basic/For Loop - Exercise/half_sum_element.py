import math

count_of_numbers = int(input())

sum_of_numbers = 0
biggest_num = -math.inf
for num in range(count_of_numbers):
    current_num = int(input())
    if current_num > biggest_num:
        biggest_num = current_num
    sum_of_numbers += current_num

sum_of_numbers -= biggest_num

if sum_of_numbers == biggest_num:
    print('Yes')
    print(f"Sum = {sum_of_numbers}")
else:
    difference = abs(biggest_num - sum_of_numbers)
    print('No')
    print(f"Diff = {difference}")
