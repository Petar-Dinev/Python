from collections import deque

petrol_pumps_count = int(input())
tank = 0
petrol_pumps = deque([])

for _ in range(petrol_pumps_count):
    petrol, distance = input().split()
    petrol_pumps.append([int(petrol), int(distance)])

for index in range(petrol_pumps_count):
    can_make_full_circle = True
    for i in range(petrol_pumps_count):
        current_petrol, current_distance = petrol_pumps[i]
        tank += current_petrol
        if current_distance <= tank:
            tank -= current_distance
        else:
            can_make_full_circle = False
            break
    if can_make_full_circle:
        print(index)
        break
    else:
        petrol_pumps.rotate(-1)
        tank = 0
