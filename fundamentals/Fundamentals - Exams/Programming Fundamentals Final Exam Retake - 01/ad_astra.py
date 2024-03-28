import re

text = input()
total_calories = 0
need_calories_per_day_in_space = 2000
pattern = r"([#|])(?P<food>[A-Za-z ]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"

matches = re.finditer(pattern, text)

for match_ in matches:
    total_calories += int(match_.group('calories'))

days_can_live_in_space = total_calories // need_calories_per_day_in_space

print(f"You have food to last you for: {days_can_live_in_space} days!")
matches = re.finditer(pattern, text)
for match in matches:
    print(f"Item: {match.group('food')}, Best before: {match.group('date')}, Nutrition: {match.group('calories')}")
