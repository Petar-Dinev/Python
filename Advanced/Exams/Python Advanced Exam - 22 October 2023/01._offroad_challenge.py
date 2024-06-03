from collections import deque

initial_fuel = [int(el) for el in input().split()]
consumption_indexes = deque([int(el) for el in input().split()])
needed_fuel = deque([int(el) for el in input().split()])

current_altitude = 0

while initial_fuel:
    difference = initial_fuel.pop() - consumption_indexes.popleft()
    if difference >= needed_fuel[0]:
        current_altitude += 1
        print(f"John has reached: Altitude {current_altitude}")
    else:
        print(f"John did not reach: Altitude {current_altitude + 1}")
        break
    needed_fuel.popleft()

if needed_fuel:
    print('John failed to reach the top.')
    if current_altitude == 0:
        print("John didn't reach any altitude.")
    else:
        result = [f"Altitude {altitude}" for altitude in range(1, current_altitude + 1)]
        print(f'Reached altitudes: {", ".join(result)}')
else:
    print("John has reached all the altitudes and managed to reach the top!")
