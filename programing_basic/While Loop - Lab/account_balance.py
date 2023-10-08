total_money = 0

current_data = input()

while current_data != 'NoMoreMoney':
    current_data = float(current_data)

    if current_data < 0:
        print('Invalid operation!')
        break
    print(f"Increase: {current_data:.2f}")
    total_money += current_data
    current_data = input()

print(f"Total: {total_money:.2f}")
