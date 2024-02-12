def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum_of_nums, num3):
    return sum_of_nums - num3


def add_and_subtract(first_num, second_num, third_num):
    result = sum_numbers(first_num, second_num)
    print(subtract(result, third_num))


first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)
