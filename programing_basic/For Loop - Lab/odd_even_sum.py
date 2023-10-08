nums = int(input())

odd_sum = 0
even_sum = 0

for num in range(nums):
    current_num = int(input())
    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

difference = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {difference}")

