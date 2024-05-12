from collections import deque

current_food = int(input())
orders = deque([int(order) for order in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()
    if current_food >= order:
        current_food -= order
    else:
        print('Orders left:', order, *orders)
        break
else:
    print("Orders complete")
