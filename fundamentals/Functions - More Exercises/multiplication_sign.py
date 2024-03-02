def find_type_of_result(num1, num2, num3):
    nums = [num1, num2, num3]

    if 0 in nums:
        return 'zero'
    else:
        count_of_negative_nums = 0
        for num in nums:
            if num < 0:
                count_of_negative_nums += 1

        if count_of_negative_nums % 2 == 0:
            return 'positive'
        else:
            return 'negative'


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(find_type_of_result(number1, number2, number3))
