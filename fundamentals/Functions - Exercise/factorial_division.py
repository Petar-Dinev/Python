def find_factorial_of_num(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def return_division_of_two_nums(num1, num2):
    num1_factorial = find_factorial_of_num(num1)
    num2_factorial = find_factorial_of_num(num2)
    division = num1_factorial // num2_factorial
    print(f'{division:.2f}')


first_num = int(input())
second_num = int(input())
return_division_of_two_nums(first_num, second_num)
