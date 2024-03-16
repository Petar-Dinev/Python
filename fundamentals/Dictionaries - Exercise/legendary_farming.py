key_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
junks = {}
is_found = False
materials = input().split()

while not is_found:

    for i in range(0, len(materials), 2):

        quantity = int(materials[i])
        material = materials[i + 1].lower()

        if material == 'shards' or material == 'fragments' or material == 'motes':
            key_materials[material] += quantity
            if key_materials['shards'] >= 250 or key_materials['fragments'] >= 250 or key_materials['motes'] >= 250:
                is_found = True
                break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity

    if is_found:
        break
    materials = input().split()

item_found = ''

if key_materials['shards'] >= 250:
    item_found = 'Shadowmourne'
    key_materials['shards'] -= 250
elif key_materials['fragments'] >= 250:
    item_found = 'Valanyr'
    key_materials['fragments'] -= 250
elif key_materials['motes'] >= 250:
    item_found = 'Dragonwrath'
    key_materials['motes'] -= 250

print(f"{item_found} obtained!")

for key, value in key_materials.items():
    print(f"{key}: {value}")

for key, value in junks.items():
    print(f"{key}: {value}")
