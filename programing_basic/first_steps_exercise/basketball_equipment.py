annual_tax_for_training_basketball = int(input())

snickers_price = annual_tax_for_training_basketball * 0.6
outfit_price = snickers_price * 0.8
ball_price = outfit_price / 4
accessories = ball_price / 5

total_cost = snickers_price + outfit_price + ball_price + accessories + annual_tax_for_training_basketball
print(total_cost)