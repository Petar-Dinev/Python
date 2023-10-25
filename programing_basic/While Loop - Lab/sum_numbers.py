number = int(input())

sum_of_nums = 0

current_num = int(input())
sum_of_nums += current_num

while sum_of_nums < number:
    current_num = int(input())
    sum_of_nums += current_num

print(sum_of_nums)