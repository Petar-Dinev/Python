sequence = input()

for i in range(len(sequence)):
    if sequence[i] == ':':
        print(f":{sequence[i + 1]}")
