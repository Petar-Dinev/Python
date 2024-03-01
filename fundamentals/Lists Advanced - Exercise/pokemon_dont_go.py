def modify_arr(arr, value):
    for i in range(len(arr)):
        if arr[i] > value:
            arr[i] -= value
        else:
            arr[i] += value
    return arr


nums = [int(num) for num in input().split()]
result = 0

while len(nums) > 0:
    index = int(input())
    current_value = 0
    if index < 0:
        current_value = nums[0]
        nums[0] = nums[-1]
    elif index >= len(nums):
        current_value = nums[-1]
        nums[-1] = nums[0]
    else:
        current_value = nums[index]
        nums.pop(index)
    nums = modify_arr(nums, current_value)
    result += current_value

print(result)
