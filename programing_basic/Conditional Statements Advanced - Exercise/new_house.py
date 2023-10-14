type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if type_of_flowers == 'Roses':
    price = 5
    if flowers_count > 80:
        price *= 0.9
elif type_of_flowers == 'Dahlias':
    price = 3.8
    if flowers_count > 90:
        price *= 0.85
elif type_of_flowers == 'Tulips':
    price = 2.8
    if flowers_count > 80:
        price *= 0.85
elif type_of_flowers == 'Narcissus':
    price = 3
    if flowers_count < 120:
        price *= 1.15
elif type_of_flowers == 'Gladiolus':
    price = 2.5
    if flowers_count < 80:
        price *= 1.2

total = price * flowers_count
difference = abs(total - budget)
if budget >= total:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")

