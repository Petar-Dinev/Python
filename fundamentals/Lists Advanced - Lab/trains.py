wagons = [0 for i in range(int(input()))]
line = input()

while line != 'End':
    tokens = line.split()
    command = tokens[0]

    if command == 'add':
        people = int(tokens[1])
        wagons[-1] += people
    elif command == 'insert':
        index = int(tokens[1])
        people = int(tokens[2])
        wagons[index] += people
    elif command == 'leave':
        index = int(tokens[1])
        people = int(tokens[2])
        wagons[index] -= people

    line = input()

print(wagons)
