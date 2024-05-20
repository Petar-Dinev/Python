from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

while bees and nectar:
    if nectar[-1] < bees[0]:
        nectar.pop()
        continue
    current_symbol = symbols.popleft()
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_symbol == '+':
        honey += abs(current_bee + current_nectar)
    elif current_symbol == '-':
        honey += abs(current_bee - current_nectar)
    elif current_symbol == '*':
        honey += abs(current_bee * current_nectar)
    elif current_symbol == '/':
        if current_nectar != 0:
            honey += abs(current_bee / current_nectar)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
