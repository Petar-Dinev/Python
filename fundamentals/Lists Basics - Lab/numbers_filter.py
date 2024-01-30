count_of_numbers = int(input())

list_of_nums = []
result = []

for i in range(count_of_numbers):
    list_of_nums.append(int(input()))

command = input()

for num in list_of_nums:
    if command == 'odd' and num % 2 != 0:
        result.append(num)
    elif command == 'even' and num % 2 == 0:
        result.append(num)
    elif command == 'positive' and num >= 0:
        result.append(num)
    elif command == 'negative' and num < 0:
        result.append(num)

print(result)
