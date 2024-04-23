sequence = input()
my_list = []

for i in range(len(sequence) - 1, -1, -1):
    my_list.append(sequence[i])

print(''.join(my_list))
