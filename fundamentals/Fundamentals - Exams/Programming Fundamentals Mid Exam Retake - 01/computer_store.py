command = input()
cost_without_taxes = 0

while command != 'regular' and command != 'special':
    price = float(command)
    command = input()
    if price < 0:
        print('Invalid price!')
        continue
    cost_without_taxes += price

if cost_without_taxes > 0:
    taxes = cost_without_taxes * 0.2
    total_cost = cost_without_taxes + taxes

    if command == 'special':
        total_cost *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {cost_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_cost:.2f}$')
else:
    print('Invalid order!')
