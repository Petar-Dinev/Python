size_of_airspace = int(input())

airspace = []
our_jet_position = []
enemies = []

for row in range(size_of_airspace):
    airspace.append(list(input()))
    for col in range(size_of_airspace):
        if airspace[row][col] == 'J':
            our_jet_position = [row, col]
        elif airspace[row][col] == 'E':
            enemies.append([row, col])

max_jet_health = 300
our_jet_health = max_jet_health

commands = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while enemies and our_jet_health:
    command = input()
    row = our_jet_position[0] + commands[command][0]
    col = our_jet_position[1] + commands[command][1]

    if airspace[row][col] == 'R':
        our_jet_health = max_jet_health
    elif airspace[row][col] == 'E':
        our_jet_health -= 100
        enemies.remove([row, col])

    airspace[our_jet_position[0]][our_jet_position[1]] = '-'
    airspace[row][col] = 'J'
    our_jet_position = [row, col]

if our_jet_health:
    print("Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates {our_jet_position}!")

[print(''.join(row)) for row in airspace]
