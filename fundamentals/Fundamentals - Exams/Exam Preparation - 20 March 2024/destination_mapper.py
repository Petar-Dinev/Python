import re

text = input()
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"

matches = re.findall(pattern, text)
travel_points = 0
destinations = []
for current_match in matches:
    current_destination = current_match[1]
    destinations.append(current_destination)
    travel_points += len(current_destination)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
