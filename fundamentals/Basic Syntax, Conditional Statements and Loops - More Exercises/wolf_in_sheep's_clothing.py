animals_list = input().split(', ')
index = 0
animals_list.reverse()
current_sheep = 0

while animals_list[index] != 'wolf':
    current_sheep += 1
    index += 1

if current_sheep == 0:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {current_sheep}! You are about to be eaten by a wolf!')
