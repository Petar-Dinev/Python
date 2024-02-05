list_of_cells = input().split('#')
amount_of_water = int(input())
effort = 0
total_fire = 0
putting_out_cells = []
for cell in list_of_cells:
    is_valid_cell = False
    type_of_cell, value = cell.split(' = ')
    value = int(value)
    if amount_of_water < value:
        continue
    if type_of_cell == 'High':
        if 80 < value <= 125:
            is_valid_cell = True
    elif type_of_cell == 'Medium':
        if 50 < value <= 80:
            is_valid_cell = True
    elif type_of_cell == 'Low':
        if 1 <= value <= 50:
            is_valid_cell = True
    if is_valid_cell:
        amount_of_water -= value
        putting_out_cells.append(value)
        effort += value * 0.25
        total_fire += value

print('Cells:')
for cell in putting_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
