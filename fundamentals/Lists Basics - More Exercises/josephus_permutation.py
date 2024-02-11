nums = [int(num) for num in input().split()]
index_for_execute = int(input()) - 1
current_index_to_execute = index_for_execute
executed_nums = []

while len(nums) > 0:
    while current_index_to_execute >= len(nums):
        current_index_to_execute -= len(nums)
    executed_nums.append(nums.pop(current_index_to_execute))
    current_index_to_execute += index_for_execute

print('[', end='')
for index in range(len(executed_nums) - 1):
    print(f'{executed_nums[index]},', end='')
print(f"{executed_nums[-1]}]")
