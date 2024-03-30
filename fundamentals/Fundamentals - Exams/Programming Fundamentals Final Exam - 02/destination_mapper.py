import re

destinations = input()
pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'

matches = re.finditer(pattern, destinations)
valid_places = []
travel_points = 0
for match in matches:
    valid_places.append(match.group(2))
    travel_points += len(match.group(2))

print(f"Destinations: {', '.join(valid_places)}")
print(f"Travel Points: {travel_points}")
