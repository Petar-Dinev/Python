travel_routes = input().split('||')
current_fuel = int(input())
current_ammunition = int(input())

for current_route in travel_routes:
    if current_route == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break

    command, value = current_route.split()

    if command == 'Travel':
        light_years_to_travel = int(value)
        if current_fuel >= light_years_to_travel:
            print(f"The spaceship travelled {light_years_to_travel} light-years.")
            current_fuel -= light_years_to_travel
        else:
            print("Mission failed.")
            break
    elif command == 'Enemy':
        enemy_armor = int(value)
        if current_ammunition >= enemy_armor:
            print(f"An enemy with {enemy_armor} armour is defeated.")
            current_ammunition -= enemy_armor
        elif current_fuel >= (enemy_armor * 2):
            print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            current_fuel -= (enemy_armor * 2)
        else:
            print("Mission failed.")
            break
    elif command == 'Repair':
        fuel_to_add = int(value)
        ammunition_to_add = int(value) * 2
        current_fuel += fuel_to_add
        current_ammunition += ammunition_to_add
        print(f"Ammunitions added: {ammunition_to_add}.")
        print(f"Fuel added: {fuel_to_add}.")
