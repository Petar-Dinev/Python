nums_as_string = input().split(' ')
result = []

for current_num in nums_as_string:
    num = int(current_num) * -1
    result.append(num)

print(result)
