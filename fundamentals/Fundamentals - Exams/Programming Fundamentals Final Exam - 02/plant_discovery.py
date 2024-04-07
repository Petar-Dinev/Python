plants_count = int(input())
plants = {}

for i in range(plants_count):
    plant_name, plant_rarity = input().split('<->')
    if plant_name not in plants:
        plants[plant_name] = {
            'ratings': []
        }
    plants[plant_name]['rarity'] = int(plant_rarity)

line = input()

while line != 'Exhibition':
    command, plant_info = line.split(': ')
    tokens = plant_info.split(' - ')
    plant_name = tokens[0]
    if plant_name not in plants:
        print('error')
    else:
        plant = plants[plant_name]
        if command == 'Rate':
            plant['ratings'].append(int(tokens[1]))
        elif command == 'Update':
            plant['rarity'] = int(tokens[1])
        elif command == 'Reset':
            plant['ratings'].clear()
    line = input()

print('Plants for the exhibition:')
for plant_name, plant_info in plants.items():
    if len(plant_info['ratings']) > 0:
        avg_ratings = sum(plant_info['ratings']) / len(plant_info['ratings'])
    else:
        avg_ratings = 0
    print(f"- {plant_name}; Rarity: {plant_info['rarity']}; Rating: {avg_ratings:.2f}")
