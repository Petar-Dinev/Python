nums = [int(num) for num in input().split()]
command = input()

while command != 'end':
    tokens = command.split()
    if tokens[0] == 'swap':
        index_one = int(tokens[1])
        index_two = int(tokens[2])
        nums[index_one], nums[index_two] = nums[index_two], nums[index_one]
    elif tokens[0] == 'multiply':
        index_one = int(tokens[1])
        index_two = int(tokens[2])
        nums[index_one] *= nums[index_two]
    else:
        nums = [num - 1 for num in nums]
    command = input()

print(*nums, sep=', ')
