first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

lines_count = int(input())

for _ in range(lines_count):
    line = input().split()
    command = line[0] + ' ' + line[1]
    nums = set([int(x) for x in line[2:]])
    if command == 'Add First':
       first_sequence.update(nums)
    elif command == 'Add Second':
       second_sequence.update(nums)
    elif command == 'Remove First':
        first_sequence.difference_update(nums)
    elif command == 'Remove Second':
        second_sequence.difference_update(nums)
    elif command == 'Check Subset':
        print(first_sequence.issubset(second_sequence) or first_sequence.issuperset(second_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
