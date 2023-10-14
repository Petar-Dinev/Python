days = int(input())
type_of_room = input()
rating = input()

nights = days - 1
price = 0

if type_of_room == 'room for one person':
    price = 18
elif type_of_room == 'apartment':
    price = 25
    if nights < 10:
        price *= 0.7
    elif nights < 15:
        price *= 0.65
    else:
        price *= 0.5
elif type_of_room == 'president apartment':
    price = 35
    if nights < 10:
        price *= 0.9
    elif nights < 15:
        price *= 0.85
    else:
        price *= 0.8

total_cost = nights * price

if rating == 'positive':
    total_cost *= 1.25
else:
    total_cost *= 0.9

print(f"{total_cost:.2f}")
