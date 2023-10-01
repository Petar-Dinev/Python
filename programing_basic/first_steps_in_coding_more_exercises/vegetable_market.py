price_of_kilo_vegetables = float(input())
price_of_kilo_fruits = float(input())
kilos_of_vegetables = int(input())
kilos_of_fruits = int(input())

total_cost_in_levs = price_of_kilo_vegetables * kilos_of_vegetables + price_of_kilo_fruits * kilos_of_fruits
total_cost_in_euro = total_cost_in_levs / 1.94
print(f"{total_cost_in_euro:.2f}")
