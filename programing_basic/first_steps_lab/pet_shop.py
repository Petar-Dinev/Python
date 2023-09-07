price_of_package_dog_food = 2.5
price_of_package_cat_food = 4
number_of_package_dog_food = int(input())
number_of_package_cat_food = int(input())
total_money_for_dog_food = number_of_package_dog_food * price_of_package_dog_food
total_money_for_cat_food = number_of_package_cat_food * price_of_package_cat_food
total = total_money_for_dog_food + total_money_for_cat_food

print(f"{total} lv.")