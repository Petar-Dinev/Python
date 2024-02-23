houses = [int(num) for num in input().split('@')]
current_input = input()
current_index = 0
while current_input != 'Love!':
    command, jump_value = current_input.split()
    jump_value = int(jump_value)
    if jump_value + current_index >= len(houses):
        current_index = 0
    else:
        current_index += jump_value
    if houses[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses[current_index] -= 2
        if houses[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    current_input = input()

print(f"Cupid's last position was {current_index}.")
count_of_houses_with_valentine_day = houses.count(0)
if count_of_houses_with_valentine_day == len(houses):
    print("Mission was successful.")
else:
    house_without_valentine_day = len(houses) - count_of_houses_with_valentine_day
    print(f"Cupid has failed {house_without_valentine_day} places.")
