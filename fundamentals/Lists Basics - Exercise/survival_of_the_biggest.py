import math
list_of_nums = [int(num) for num in input().split()]
nums_to_remove = int(input())

for _ in range(nums_to_remove):
    current_lowest_num = math.inf

    for i in range(len(list_of_nums)):
        if list_of_nums[i] < current_lowest_num:
            current_lowest_num = list_of_nums[i]

    list_of_nums.remove(current_lowest_num)

for i in range(len(list_of_nums) - 1):
    print(list_of_nums[i], end=', ')
print(list_of_nums[-1])
