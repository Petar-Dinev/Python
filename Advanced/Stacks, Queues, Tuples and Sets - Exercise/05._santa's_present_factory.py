from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

present_magic_needed = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}
presents_made = {}

while materials and magic_levels:
    product = materials[-1] * magic_levels[0]

    if product < 0:
        materials.append(materials.pop() + magic_levels.popleft())
    elif product > 0:
        is_made_present = False
        for key, value in present_magic_needed.items():
            if product == value:
                if key not in presents_made:
                    presents_made[key] = 0
                presents_made[key] += 1
                is_made_present = True
        if is_made_present:
            magic_levels.popleft()
            materials.pop()
        else:
            magic_levels.popleft()
            materials[-1] += 15
    else:
        if magic_levels[0] == 0 and materials[-1] == 0:
            magic_levels.popleft()
            materials.pop()
        elif magic_levels[0] == 0:
            magic_levels.popleft()
        elif materials[-1] == 0:
            materials.pop()


if ('Doll' in presents_made.keys() and 'Wooden train' in presents_made) or ('Teddy bear' in presents_made and 'Bicycle' in presents_made):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in materials]))}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for key, value in sorted(presents_made.items()):
    print(f"{key}: {value}")
