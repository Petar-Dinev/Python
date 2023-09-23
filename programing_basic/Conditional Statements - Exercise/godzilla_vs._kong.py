budget = float(input())
number_of_extras = int(input())
price_of_one_dress = float(input())

decor_price = budget * 0.1
total_cost_for_dress = number_of_extras * price_of_one_dress

if number_of_extras > 150:
    total_cost_for_dress *= 0.9

total_cost = total_cost_for_dress + decor_price
difference = abs(budget - total_cost)

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
