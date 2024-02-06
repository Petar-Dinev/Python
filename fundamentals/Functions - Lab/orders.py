def calculate_total_price(product, quantity):
    price_of_product = 0

    if product == 'coffee':
        price_of_product = 1.5
    elif product == 'water':
        price_of_product = 1
    elif product == 'coke':
        price_of_product = 1.4
    elif product == 'snacks':
        price_of_product = 2

    total_price = price_of_product * quantity
    return f'{total_price:.2f}'


input_product = input()
quantity_of_product = int(input())
print(calculate_total_price(input_product, quantity_of_product))
