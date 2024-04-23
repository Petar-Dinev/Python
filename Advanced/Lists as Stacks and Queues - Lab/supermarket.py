queue = []
line = input()

while line != 'End':
    if line == 'Paid':
        print('\n'.join(queue))
        queue.clear()
    else:
        queue.append(line)
    line = input()

print(f"{len(queue)} people remaining.")
