products = {}

while True:
    command = input()
    if command == 'statistics':
        break
    product, quantity = command.split(': ')
    if product not in products:
        products[product] = 0
    products[product] += int(quantity)

print('Products in stock:')
for key, value in products.items():
    print(f"- {key}: {value}")
total_products = len(products.keys())
print(f"Total Products: {total_products}")
total_quantity = sum(list(products.values()))
print(f"Total Quantity: {total_quantity}")
