elements = input().split()
products = {}

for i in range(0, len(elements), 2):
    if elements[i] not in products.keys():
        products[elements[i]] = 0
    products[elements[i]] += int(elements[i + 1])

search_products = input().split()

for product in search_products:
    if product in products.keys():
        quantity = products[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f'Sorry, we don\'t have {product}')
