nums_list = [int(num) for num in (input().split(', '))]

result = []
zero_list = []

for num in nums_list:
    if num == 0:
        zero_list.append(num)
    else:
        result.append(num)

print(result + zero_list)
