items_to_buy = input().split('|')
budget = float(input())
buys_items = []
profit = 0
total_money = 0

for current_item in items_to_buy:
    type_of_item, price = current_item.split('->')
    price = float(price)
    if type_of_item == 'Clothes' and price <= 50 or type_of_item == 'Shoes' and price <= 35 \
            or type_of_item == 'Accessories' and price <= 20.50:
        if budget >= price:
            budget -= price
            buys_items.append(price * 1.4)
            profit += price * 0.4

for buy_item in buys_items:
    total_money += buy_item
    print(f'{buy_item:.2f}', end=" ")

print()
print(f'Profit: {profit:.2f}')
if (total_money + budget) >= 150:
    print('Hello, France!')
else:
    print("Not enough money.")
