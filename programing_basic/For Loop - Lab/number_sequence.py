import sys

num_of_numbers = int(input())

smallest_num = sys.maxsize
biggest_num = -sys.maxsize

for _ in range(num_of_numbers):
    current_num = int(input())
    if current_num > biggest_num:
        biggest_num = current_num
    if current_num < smallest_num:
        smallest_num = current_num

print(f"Max number: {biggest_num}")
print(f"Min number: {smallest_num}")
