command = input()
money = 0

while command != 'End':
    destination = command
    price_of_vacation = float(input())

    while money < price_of_vacation:
        saved_money = float(input())
        money += saved_money
        if money >= price_of_vacation:
            print(f"Going to {destination}!")
            money = 0
            break
    command = input()
