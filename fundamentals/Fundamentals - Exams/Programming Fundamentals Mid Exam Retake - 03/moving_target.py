targets = [int(num) for num in input().split()]
current_input = input()

while current_input != 'End':
    tokens = current_input.split()
    command = tokens[0]
    index = int(tokens[1])
    current_input = input()
    if command == 'Shoot' and 0 <= index < len(targets):
        power = int(tokens[2])
        if targets[index] > power:
            targets[index] -= power
        else:
            targets.pop(index)
    elif command == 'Add':
        value = int(tokens[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == 'Strike':
        radius = int(tokens[2])
        if index + radius >= len(targets) or index - radius < 0:
            print("Strike missed!")
        else:
            start_index = index + radius + 1
            end_index = index - radius
            targets = targets[:end_index] + targets[start_index:]

for i in range(len(targets)):
    if i == len(targets) - 1:
        print(targets[i])
    else:
        print(targets[i], end='|')
