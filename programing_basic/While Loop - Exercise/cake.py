cake_width = int(input())
cake_length = int(input())
cake_volume = cake_length * cake_width

while cake_volume > 0:
    command = input()
    if command == 'STOP':
        print(f"{cake_volume} pieces are left.")
        break
    peaces_of_cake = int(command)
    cake_volume -= peaces_of_cake
else:
    print(f"No more cake left! You need {abs(cake_volume)} pieces more.")

