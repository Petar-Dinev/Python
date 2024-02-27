energy = int(input())
current_input = input()
won_battles_count = 0

while current_input != 'End of battle':
    distance_to_enemy = int(current_input)
    if energy >= distance_to_enemy:
        won_battles_count += 1
        energy -= distance_to_enemy
    else:
        print(f"Not enough energy! Game ends with {won_battles_count} won battles and {energy} energy")
        break
    if won_battles_count % 3 == 0:
        energy += won_battles_count
    current_input = input()
else:
    print(f"Won battles: {won_battles_count}. Energy left: {energy}")
