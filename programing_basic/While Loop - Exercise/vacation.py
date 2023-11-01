money_for_vacation = float(input())
total_money = float(input())
total_days = 0
spend_days = 0
is_fail = False

while total_money < money_for_vacation:
    command = input()
    current_money = float(input())

    total_days += 1

    if command == 'save':
        total_money += current_money
        spend_days = 0
    else:
        spend_days += 1
        total_money -= current_money
        if total_money < 0:
            total_money = 0
        if spend_days == 5:
            is_fail = True
            break

if is_fail:
    print("You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
