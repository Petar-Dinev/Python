chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.5

numbers_of_chickens_menus = int(input())
numbers_of_fish_menus = int(input())
numbers_of_vegetarian_menus = int(input())
total_sum_without_desert = numbers_of_vegetarian_menus * vegetarian_menu_price + numbers_of_chickens_menus * chicken_menu_price + numbers_of_fish_menus * fish_menu_price
total_sum = total_sum_without_desert + total_sum_without_desert * 0.2 + delivery_price
print(total_sum)