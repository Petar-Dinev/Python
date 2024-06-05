size_of_matrix = int(input())

matrix = []
player_position = []

for row in range(size_of_matrix):
    matrix.append(list(input()))
    for col in range(size_of_matrix):
        if matrix[row][col] == 'P':
            player_position = [row, col]

commands = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

is_alive = True
is_escaped = False
max_player_health = 100
player_health = max_player_health
potion_health = 15
monster_dmg = 40

while is_alive and not is_escaped:
    command = input()
    row = player_position[0] + commands[command][0]
    col = player_position[1] + commands[command][1]

    if not 0 <= row < size_of_matrix or not 0 <= col < size_of_matrix:
        continue

    if matrix[row][col] == 'X':
        is_escaped = True
    elif matrix[row][col] == 'H':
        player_health += potion_health
        if player_health > 100:
            player_health = max_player_health
    elif matrix[row][col] == 'M':
        player_health -= monster_dmg
        if player_health <= 0:
            if player_health < 0:
                player_health = 0
            is_alive = False

    matrix[row][col] = 'P'
    matrix[player_position[0]][player_position[1]] = '-'
    player_position = [row, col]

if player_health > 0:
    print("Player escaped the maze. Danger passed!")
else:
    print("Player is dead. Maze over!")
print(f"Player's health: {player_health} units")
[print(''.join(row)) for row in matrix]
