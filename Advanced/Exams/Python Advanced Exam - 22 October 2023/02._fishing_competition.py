fishing_area_size = int(input())

fishing_area, ship_row, ship_col = [], 0, 0

for row in range(fishing_area_size):
    fishing_area.append(list(input()))
    if 'S' in fishing_area[row]:
        ship_row, ship_col = row, fishing_area[row].index('S')

commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}
collected_fish = 0
fish_quota = 20

is_sink = False

command = input()

while command != "collect the nets":
    next_row = ship_row + commands[command][0]
    next_col = ship_col + commands[command][1]
    if next_row == fishing_area_size:
        next_row = 0
    if next_row == -1:
        next_row = fishing_area_size - 1
    if next_col == fishing_area_size:
        next_col = 0
    if next_col == -1:
        next_col = fishing_area_size - 1

    fishing_area[ship_row][ship_col] = '-'

    ship_row = next_row
    ship_col = next_col

    if fishing_area[ship_row][ship_col] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. \
Last coordinates of the ship: [{ship_row},{ship_col}]")
        is_sink = True
        break
    elif fishing_area[ship_row][ship_col].isdigit():
        collected_fish += int(fishing_area[ship_row][ship_col])

    fishing_area[ship_row][ship_col] = 'S'

    command = input()

else:
    if collected_fish >= fish_quota:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! \
You need {fish_quota - collected_fish} tons of fish more.")

    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")

    [print(''.join(row)) for row in fishing_area]
