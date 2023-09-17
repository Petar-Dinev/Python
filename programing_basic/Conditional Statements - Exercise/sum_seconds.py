first_time = int(input())
second_time = int(input())
third_time = int(input())

total_sum = first_time + second_time + third_time
minutes = total_sum // 60
seconds = total_sum % 60

print(f"{minutes}:{seconds:02d}")
