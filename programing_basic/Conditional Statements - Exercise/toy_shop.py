price_of_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bear = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

profit_from_dolls = number_of_dolls * 3
profit_from_teddy_bears = number_of_teddy_bear * 4.1
profit_from_puzzles = number_of_puzzles * 2.6
profit_from_minions = number_of_minions * 8.2
profit_from_trucks = number_of_trucks * 2

number_of_sell_toys = number_of_trucks + number_of_minions +number_of_puzzles + number_of_dolls + number_of_teddy_bear

total_profit_without_rent = profit_from_dolls + profit_from_teddy_bears + profit_from_puzzles + profit_from_minions + profit_from_trucks

if number_of_sell_toys >= 50:
    total_profit_without_rent *= 0.75

total_profit = total_profit_without_rent * 0.9

difference = abs(total_profit - price_of_trip)

if total_profit >= price_of_trip:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")

