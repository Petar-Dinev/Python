notes = ['0' for i in range(10)]
command = input()

while command != 'End':
    tokens = command.split('-')
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)
    command = input()

result = [note for note in notes if note != '0']

print(result)
