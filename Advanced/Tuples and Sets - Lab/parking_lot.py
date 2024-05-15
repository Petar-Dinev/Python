cars_count = int(input())
cars = set()

for _ in range(cars_count):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        cars.add(car_number)
    else:
        if car_number in cars:
            cars.remove(car_number)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
