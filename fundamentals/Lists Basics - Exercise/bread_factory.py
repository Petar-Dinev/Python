events_list = input().split('|')
coins = 100
current_energy = 100

for event in events_list:
    if 'rest' in event or 'order' in event:
        event_name, quantity = event.split('-')
        quantity = int(quantity)
        if event_name == 'rest':
            gained_energy = quantity
            if current_energy + quantity > 100:
                gained_energy = 100 - current_energy
            current_energy += gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {current_energy}.")
        else:
            if current_energy >= 30:
                current_energy -= 30
                coins += quantity
                print(f"You earned {quantity} coins.")
            else:
                current_energy += 50
                if current_energy > 100:
                    current_energy = 100
                print("You had to rest!")
    else:
        ingredient, price = event.split('-')
        price = int(price)
        if coins >= price:
            coins -= price
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
