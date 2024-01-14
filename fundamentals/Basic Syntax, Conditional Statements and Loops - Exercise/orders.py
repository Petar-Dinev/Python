orders = int(input())

total = 0

for i in range(orders):
    cost_for_order = 0
    price_per_coffe = float(input())
    days = int(input())
    coffees_per_day = int(input())
    if 0.01 <= price_per_coffe <= 100 and 1 <= coffees_per_day <= 2000 and 0 < days <= 31:
        cost_for_order = price_per_coffe * coffees_per_day * days

    if cost_for_order > 0:
        print(f"The price for the coffee is: ${cost_for_order:.2f}")
        total += cost_for_order

print(f"Total: ${total:.2f}")
