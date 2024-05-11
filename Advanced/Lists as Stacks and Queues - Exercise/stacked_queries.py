queries_count = int(input())
nums = []

for i in range(queries_count):
    current_query = input().split()
    query_type = current_query[0]
    if query_type == '1':
        nums.append(int(current_query[1]))
    elif query_type == '2':
        if nums:
            nums.pop()
    elif query_type == '3':
        if nums:
            print(max(nums))
    elif query_type == '4':
        if nums:
            print(min(nums))

while nums:
    if len(nums) == 1:
        print(nums.pop())
    else:
        print(nums.pop(), end=", ")
