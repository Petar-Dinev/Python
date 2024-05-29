size_of_field = int(input())

field = []
miner_position = []
coals = []

type_of_commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

commands = input().split()

for row in range(size_of_field):
    field.append(input().split())
    for col in range(size_of_field):
        if field[row][col] == 's':
            miner_position = [row, col]
        elif field[row][col] == 'c':
            coals.append([row, col])

for command in commands:
    current_row = miner_position[0] + type_of_commands[command][0]
    current_col = miner_position[1] + type_of_commands[command][1]
    if 0 <= current_row < size_of_field and 0 <= current_col < size_of_field:
        miner_position = [current_row, current_col]
        if field[current_row][current_col] == 'c':
            field[current_row][current_col] = '*'
            coals.remove([current_row, current_col])
        elif field[current_row][current_col] == 'e':
            print(f"Game over! ({current_row}, {current_col})")
            break
else:
    if coals:
        print(f"{len(coals)} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
    else:
        print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
