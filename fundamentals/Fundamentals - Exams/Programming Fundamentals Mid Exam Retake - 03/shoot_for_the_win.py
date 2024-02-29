targets = [int(num) for num in input().split()]
count_of_shoot_targets = 0
line = input()

while line != 'End':
    index = int(line)
    if 0 <= index < len(targets):
        value_of_current_target = targets[index]
        for i in range(len(targets)):
            if targets[i] <= value_of_current_target and targets[i] != -1:
                targets[i] += value_of_current_target
            elif targets[i] > value_of_current_target:
                targets[i] -= value_of_current_target
        targets[index] = -1
        count_of_shoot_targets += 1
    line = input()

print(f'Shot targets: {count_of_shoot_targets} -> ', end='')
for target in targets:
    print(target, end=' ')
