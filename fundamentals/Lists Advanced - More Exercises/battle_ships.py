count_of_rows = int(input())
battle_ships_coordinates = []
battle_ships_kill = 0

for i in range(count_of_rows):
    current_row = [int(num) for num in input().split()]
    battle_ships_coordinates.append(current_row)

coordinates_for_attack = input().split()

for current_coordinates in coordinates_for_attack:
    row, col = current_coordinates.split('-')
    row = int(row)
    col = int(col)
    current_position = battle_ships_coordinates[row][col]
    if current_position > 0:
        battle_ships_coordinates[row][col] -= 1
        if battle_ships_coordinates[row][col] == 0:
            battle_ships_kill += 1

print(battle_ships_kill)
