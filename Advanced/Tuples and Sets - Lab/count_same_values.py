nums = [float(num) for num in input().split()]
read_nums = []

for num in nums:
    if num not in read_nums:
        read_nums.append(num)
        print(f"{num} - {nums.count(num)} times")
