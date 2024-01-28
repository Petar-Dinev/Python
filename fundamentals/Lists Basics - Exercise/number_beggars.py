values_as_string = input().split(', ')
count_of_beggars = int(input())

list_beggars_values = []

for current_beggar_index in range(count_of_beggars):
    current_beggar_sum = 0
    for index in range(current_beggar_index, len(values_as_string), count_of_beggars):
        current_beggar_sum += int(values_as_string[index])
    list_beggars_values.append(current_beggar_sum)

print(list_beggars_values)
