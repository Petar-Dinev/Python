def calculate(operator, num1, num2):
    result = 0
    if operator == 'add':
        result = num1 + num2
    elif operator == 'divide':
        if num2 != 0:
            result = int(num1 / num2)
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    return result


input_operator = input()
first_num = int(input())
second_num = int(input())
print(calculate(input_operator, first_num, second_num))
