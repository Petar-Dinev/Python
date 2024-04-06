chest = input().split('|')

line = input()

while line != 'Yohoho!':
    tokens = line.split()
    command = tokens[0]
    if command == 'Loot':
        for i in range(1, len(tokens)):
            current_loot = tokens[i]
            if current_loot not in chest:
                chest.insert(0, current_loot)
    elif command == 'Drop':
        index = int(tokens[1])
        if 0 <= index < len(chest):
            dropped_item = chest.pop(index)
            chest.append(dropped_item)
    elif command == 'Steal':
        count = int(tokens[1])
        start_stolen_index = len(chest) - count
        if start_stolen_index < 0:
            start_stolen_index = 0
        stolen_loot = chest[start_stolen_index:]
        chest = chest[:start_stolen_index]
        print(', '.join(stolen_loot))
    line = input()

average_gain = 0

for loot in chest:
    average_gain += len(loot) / len(chest)

if len(chest) > 0:
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
