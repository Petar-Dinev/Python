budget = float(input())
season = input()

destination = ''
place = ''
cost = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        cost = budget * 0.3
    else:
        place = 'Hotel'
        cost = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        cost = budget * 0.4
    else:
        place = 'Hotel'
        cost = budget * 0.8
else:
    destination = 'Europe'
    place = 'Hotel'
    cost = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {cost:.2f}")
