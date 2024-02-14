def check_if_number_is_perfect(number):
    sum_of_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return "We have a perfect number!" if sum_of_divisors == number else "It's not so perfect."


num = int(input())
print(check_if_number_is_perfect(num))
