stocks = {}
sold_foods = 0
line = input()

while line != 'Complete':
    command, quantity, food = line.split()
    quantity = int(quantity)
    if command == 'Receive':
        if quantity > 0:
            if food not in stocks:
                stocks[food] = 0
            stocks[food] += quantity
    elif command == 'Sell':
        if food not in stocks:
            print(f"You do not have any {food}.")
        else:
            current_quantity = stocks[food]
            if current_quantity < quantity:
                print(f"There aren't enough {food}. You sold the last {current_quantity} of them.")
                sold_foods += current_quantity
                del stocks[food]
            else:
                print(f"You sold {quantity} {food}.")
                stocks[food] -= quantity
                sold_foods += quantity
                if stocks[food] == 0:
                    del stocks[food]
    line = input()
for current_food in stocks:
    print(f"{current_food}: {stocks[current_food]}")
print(f"All sold: {sold_foods} goods")
