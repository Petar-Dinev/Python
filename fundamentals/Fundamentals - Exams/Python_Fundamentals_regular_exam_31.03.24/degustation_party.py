guests = {}
unliked_meals = 0

line = input()
while line != 'Stop':
    command, guest_name, meal = line.split('-')
    if command == 'Like':
        if guest_name not in guests:
            guests[guest_name] = []
        current_guest_meals_list = guests[guest_name]
        if meal not in current_guest_meals_list:
            current_guest_meals_list.append(meal)
    else:
        if guest_name not in guests:
            print(f"{guest_name} is not at the party.")
        else:
            current_guest_meals_list = guests[guest_name]
            if meal not in current_guest_meals_list:
                print(f"{guest_name} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest_name} doesn't like the {meal}.")
                current_guest_meals_list.remove(meal)
                unliked_meals += 1
    line = input()

for guest, meals in guests.items():
    print(f"{guest}: {', '.join(meals)}")
print(f'Unliked meals: {unliked_meals}')
