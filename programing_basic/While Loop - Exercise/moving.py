width = int(input())
length = int(input())
height = int(input())

apartment_volume = width * length * height

while apartment_volume > 0:
    command = input()
    if command == 'Done':
        print(f"{apartment_volume} Cubic meters left.")
        break
    boxes = int(command)
    apartment_volume -= boxes
else:
    print(f"No more free space! You need {abs(apartment_volume)} Cubic meters more.")

