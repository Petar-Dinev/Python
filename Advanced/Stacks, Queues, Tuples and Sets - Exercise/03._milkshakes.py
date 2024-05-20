from collections import deque

chocolate = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes_count = 0

while milkshakes_count < 5 and chocolate and cups_of_milk:

    if chocolate[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolate.pop()
        cups_of_milk.popleft()
        continue

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolate[-1] == cups_of_milk[0]:
        milkshakes_count += 1
        chocolate.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        # cups_of_milk.rotate(-1)
        chocolate[-1] -= 5

print("Great! You made all the chocolate milkshakes needed!" if milkshakes_count == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chocolate])}" if chocolate else "Chocolate: empty")
print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}" if cups_of_milk else "Milk: empty")
