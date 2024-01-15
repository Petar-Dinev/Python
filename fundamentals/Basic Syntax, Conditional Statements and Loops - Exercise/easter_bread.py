budget = float(input())
price_of_flour = float(input())
price_of_eggs = 0.75 * price_of_flour
price_of_milk = 1.25 * price_of_flour / 4
price_for_one_loaf = price_of_milk + price_of_flour + price_of_eggs

current_loaves = 0
colored_eggs = 0

while budget > price_for_one_loaf:
    budget -= price_for_one_loaf
    current_loaves += 1
    colored_eggs += 3

    if current_loaves % 3 == 0:
        colored_eggs -= (current_loaves - 2)

print(f"You made {current_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
