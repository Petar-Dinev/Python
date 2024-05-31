from collections import deque

henry_money = [int(el) for el in input().split()]
price_of_foods = deque([int(el) for el in input().split()])

bought_foods = 0

while henry_money and price_of_foods:
    current_money = henry_money.pop()
    current_price_of_food = price_of_foods.popleft()

    if current_money >= current_price_of_food:
        bought_foods += 1
        if henry_money:
            diff = current_money - current_price_of_food
            henry_money[-1] += diff

if bought_foods >= 4:
    print(f"Gluttony of the day! Henry ate {bought_foods} foods.")
elif bought_foods > 1:
    print(f"Henry ate: {bought_foods} foods.")
elif bought_foods > 0:
    print(f"Henry ate: {bought_foods} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
