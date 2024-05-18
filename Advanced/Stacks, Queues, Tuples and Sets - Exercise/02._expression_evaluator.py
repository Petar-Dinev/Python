from collections import deque

sequence = input().split()

nums = deque()

for el in sequence:
    if el not in '+-*/':
        nums.append(int(el))
    else:
        result = nums.popleft()

        while len(nums) > 0:
            current_num = nums.popleft()
            if el == '+':
                result += current_num
            elif el == '-':
                result -= current_num
            elif el == '*':
                result *= current_num
            elif el == '/':
                result //= current_num

        nums.append(result)

print(nums[0])
