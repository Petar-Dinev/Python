line = input()
nums = [int(char) for char in line if char.isdigit()]
string = [char for char in line if not char.isdigit()]
even_index_nums = []
odd_index_nums = []

for i in range(len(nums)):
    if i % 2 == 0:
        even_index_nums.append(nums[i])
    else:
        odd_index_nums.append(nums[i])

result = ''

for i in range(len(even_index_nums)):
    take = even_index_nums[i]
    skip = odd_index_nums[i]
    result += ''.join(string[:take])
    string = string[take + skip:]

print(result)
