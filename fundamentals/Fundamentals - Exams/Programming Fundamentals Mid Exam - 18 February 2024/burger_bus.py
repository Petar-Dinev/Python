number_of_cities = int(input())
total_profit = 0

for number_of_city in range(1, number_of_cities + 1):
    current_city_name = input()
    income_for_current_city = float(input())
    expenses_for_current_city = float(input())

    if number_of_city % 3 == 0 and number_of_city % 5 != 0:
        expenses_for_current_city *= 1.5

    if number_of_city % 5 == 0:
        income_for_current_city *= 0.9

    profit_for_current_city = income_for_current_city - expenses_for_current_city
    total_profit += profit_for_current_city
    print(f"In {current_city_name} Burger Bus earned {profit_for_current_city:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
