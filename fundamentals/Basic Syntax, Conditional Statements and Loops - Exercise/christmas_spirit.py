quantity_of_decorations_for_buys = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
ornament_set_spirit = 5
tree_skirt_price = 5
tree_skirt_spirit = 3
tree_garland_price = 3
tree_garland_spirit = 10
tree_lights_price = 15
tree_lights_spirit = 17

cost = 0
spirit = 0
current_day = 0

for i in range(days_until_christmas):
    current_day += 1

    if current_day % 11 == 0:
        quantity_of_decorations_for_buys += 2

    if current_day % 2 == 0:
        cost += quantity_of_decorations_for_buys * ornament_set_price
        spirit += ornament_set_spirit

    if current_day % 3 == 0:
        cost += quantity_of_decorations_for_buys * (tree_skirt_price + tree_garland_price)
        spirit += (tree_skirt_spirit + tree_garland_spirit)

    if current_day % 5 == 0:
        cost += quantity_of_decorations_for_buys * tree_lights_price
        spirit += tree_lights_spirit

    if current_day % 3 == 0 and current_day % 5 == 0:
        spirit += 30

    if current_day % 10 == 0:
        cost += (tree_skirt_price + tree_lights_price + tree_garland_price)
        spirit -= 20

if current_day % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
