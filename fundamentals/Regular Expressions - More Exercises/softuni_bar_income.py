import re

total_money = 0

line = input()
pattern = r"(%[A-Z][a-z]+%).*(\<\w+\>).*(\|\d+\|)[a-z]*(\d+0?\.?\d+\$)"

while line != 'end of shift':

    match = re.match(pattern, line)
    if match is not None:
        customer = match[1][1:-1]
        product = match[2][1:-1]
        count = int(match[3][1:-1])
        price = float(match[4][:-1])

        current_total_price = count * price
        total_money += current_total_price

        print(f"{customer}: {product} - {current_total_price:.2f}")

    line = input()

print(f'Total income: {total_money:.2f}')
