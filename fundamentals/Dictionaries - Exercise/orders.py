command = input()
products = {}

while command != 'buy':
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {
            'price': 0.0,
            'quantity': 0
        }

    products[product]['price'] = price
    products[product]['quantity'] += quantity

    command = input()

for product in products:
    product_sum = products[product]['price'] * products[product]['quantity']
    print(f"{product} -> {product_sum:.2f}")
