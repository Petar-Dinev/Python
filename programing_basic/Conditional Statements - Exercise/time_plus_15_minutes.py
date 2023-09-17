hours = int(input())
minutes = int(input())
minutes += 15
hours += minutes // 60
minutes %= 60
if hours > 23:
    hours = 0
print(f"{hours}:{minutes:02d}")
