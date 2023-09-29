age_of_lily = int(input())
price_of_washing_machine = float(input())
price_of_one_toy = int(input())

money_from_birthdays = 0
current_money_gift_for_birthday = 0
toys_count = 0

for age in range(1, age_of_lily + 1):
    if age % 2 == 0:
        current_money_gift_for_birthday += 10
        money_from_birthdays += current_money_gift_for_birthday - 1
    else:
       toys_count  += 1

total_lily_money = money_from_birthdays + toys_count * price_of_one_toy
difference = abs(total_lily_money - price_of_washing_machine)

if total_lily_money >= price_of_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
