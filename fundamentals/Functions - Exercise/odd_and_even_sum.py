def print_sums_of_odd_and_even_nums_in_number(number):
    num_as_string = str(number)

    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for current_digit_as_string in num_as_string:
        current_digit = int(current_digit_as_string)
        if int(current_digit) % 2 == 0:
            sum_of_even_digits += current_digit
        else:
            sum_of_odd_digits += current_digit

    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")


num = int(input())

print_sums_of_odd_and_even_nums_in_number(num)
