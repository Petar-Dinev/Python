targets = {}

line = input()

while line != 'Sail':
    city, population, gold = line.split('||')
    if city not in targets:
        targets[city] = {
            'population': 0,
            'gold': 0
        }
    targets[city]['population'] += int(population)
    targets[city]['gold'] += int(gold)
    line = input()

line = input()

while line != 'End':
    tokens = line.split('=>')
    command = tokens[0]
    town = tokens[1]
    if command == 'Plunder':
        people = int(tokens[2])
        gold = int(tokens[3])

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        targets[town]['population'] -= people
        targets[town]['gold'] -= gold

        if targets[town]['gold'] == 0 or targets[town]['population'] == 0:
            print(f"{town} has been wiped off the map!")
            del targets[town]
    elif command == 'Prosper':
        gold = int(tokens[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targets[town]['gold'] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {targets[town]['gold']} gold.")
    line = input()
if len(targets.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(targets.keys())} wealthy settlements to go to:")
    for town, info in targets.items():
        print(f"{town} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
