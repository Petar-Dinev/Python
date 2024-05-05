food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
guinea_weight_in_grams = float(input()) * 1000
days = 30

for i in range(1, days + 1):
    food_in_grams -= 300
    if i % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if i % 3 == 0:
        cover_in_grams -= guinea_weight_in_grams / 3
    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        print("Merry must go to the pet store!")
        break
else:
    food_in_kilos = food_in_grams / 1000
    hay_in_kilos = hay_in_grams / 1000
    cover_in_kilos = cover_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kilos:.2f}, Hay: {hay_in_kilos:.2f}, \
Cover: {cover_in_kilos:.2f}.")
