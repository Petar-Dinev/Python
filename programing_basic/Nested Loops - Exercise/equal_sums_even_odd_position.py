num1 = int(input())
num2 = int(input())

for num in range(num1, num2 + 1):
    num_in_string = str(num)
    odd_sum = 0
    even_sum = 0
    for index in range(len(num_in_string)):
        digit = int(num_in_string[index])
        if index % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if odd_sum == even_sum:
        print(num, end=" ")
