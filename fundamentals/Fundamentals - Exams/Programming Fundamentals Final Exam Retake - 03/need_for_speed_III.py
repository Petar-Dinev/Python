cars_count = int(input())
cars = {}

for i in range(cars_count):
    car_name, mileage, fuel = input().split('|')
    cars[car_name] = {
        'mileage': int(mileage),
        'fuel': int(fuel)
    }

line = input()

while line != 'Stop':
    tokens = line.split(' : ')
    command = tokens[0]
    current_car_name = tokens[1]
    car = cars[current_car_name]

    if command == 'Drive':
        distance = int(tokens[2])
        needed_fuel = int(tokens[3])
        if car['fuel'] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            car['mileage'] += distance
            car['fuel'] -= needed_fuel
            print(f"{current_car_name} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if car['mileage'] >= 100000:
                del cars[current_car_name]
                print(f"Time to sell the {current_car_name}!")
    elif command == 'Refuel':
        refilled_fuel = int(tokens[2])
        current_fuel = car['fuel']
        car['fuel'] += refilled_fuel
        if car['fuel'] > 75:
            car['fuel'] = 75
            refilled_fuel = 75 - current_fuel
        print(f"{current_car_name} refueled with {refilled_fuel} liters")
    elif command == 'Revert':
        kilometers = int(tokens[2])
        car['mileage'] -= kilometers
        if car['mileage'] >= 10000:
            print(f"{current_car_name} mileage decreased by {kilometers} kilometers")
        else:
            car['mileage'] = 10000
    line = input()

for car, car_info in cars.items():
    print(f"{car} -> Mileage: {car_info['mileage']} kms, Fuel in the tank: {car_info['fuel']} lt.")
