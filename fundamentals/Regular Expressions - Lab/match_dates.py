import re

dates = input()
pattern = r'\b(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})\b'
valid_dates = re.finditer(pattern, dates)
print(valid_dates)
for date in valid_dates:
    print(date)
    print(date[0])
    print(date[1])
    print(date[2])
    print(date[3])
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
