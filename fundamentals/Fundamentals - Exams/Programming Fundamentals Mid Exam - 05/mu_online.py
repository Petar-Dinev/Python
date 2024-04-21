health = 100
coins = 0

rooms = input().split('|')

for i in range(len(rooms)):
    command, quantity = rooms[i].split()
    quantity = int(quantity)

    if command == 'potion':
        current_health = health
        healed_health = quantity
        if health + quantity > 100:
            healed_health = (100 - current_health)
        health += healed_health
        print(f"You healed for {healed_health} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        coins += quantity
        print(f"You found {quantity} bitcoins.")
    else:
        health -= quantity
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
