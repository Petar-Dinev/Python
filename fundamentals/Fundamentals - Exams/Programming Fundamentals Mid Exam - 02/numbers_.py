nums = [int(num) for num in input().split()]
average_value = sum(nums) // len(nums)
result = []

for num in nums:
    if num > average_value:
        result.append(num)

if not result:
    print('No')
else:
    print(*sorted(result, reverse=True)[:5], sep=' ')
