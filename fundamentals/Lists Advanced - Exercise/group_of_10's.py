nums = [int(num) for num in input().split(', ')]

boundary = 0

while nums:
    current_group = [num for num in nums if boundary <= num <= (boundary + 10)]
    boundary += 10
    nums = [num for num in nums if num > boundary]
    print(f"Group of {boundary}'s: {current_group}")
