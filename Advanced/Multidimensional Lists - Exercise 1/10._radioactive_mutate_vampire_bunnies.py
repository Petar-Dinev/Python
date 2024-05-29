rows, cols = [int(x) for x in input().split()]

lair = []
player_position = []
bunnies = []

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    "R": (0, 1),
    'L': (0, -1)
}

is_player_alive = True
is_escaped = False

for row in range(rows):
    lair.append(list(input()))
    for col in range(cols):
        if lair[row][col] == 'P':
            player_position = [row, col]
        elif lair[row][col] == 'B':
            bunnies.append([row, col])

commands = list(input())

for command in commands:
    current_row = player_position[0] + moves[command][0]
    current_col = player_position[1] + moves[command][1]
    lair[player_position[0]][player_position[1]] = '.'

    if 0 <= current_row < rows and 0 <= current_col < cols:
        if lair[current_row][current_col] == 'B':
            is_player_alive = False
        else:
            lair[current_row][current_col] = 'P'
        player_position = [current_row, current_col]
    else:
        is_escaped = True

    current_bunnies = []

    for bunny in bunnies:
        for _, values in moves.items():
            row = bunny[0] + values[0]
            col = bunny[1] + values[1]
            if 0 <= row < rows and 0 <= col < cols:
                current_bunnies.append([row, col])
                if lair[row][col] == 'P':
                    is_player_alive = False
                lair[row][col] = 'B'

    bunnies = current_bunnies

    if is_escaped or not is_player_alive:
        break

[print(''.join(row)) for row in lair]

if is_escaped:
    print(f"won: {player_position[0]} {player_position[1]}")
else:
    print(f"dead: {player_position[0]} {player_position[1]}")
