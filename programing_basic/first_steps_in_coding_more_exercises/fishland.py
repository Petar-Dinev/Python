mackerel_price = float(input())
sprat_price = float(input())
bonito_kilograms = float(input())
scad_kilograms = float(input())
mussels_kilograms = int(input())
bonito_price = mackerel_price * 1.6
scad_price = sprat_price * 1.8
mussels_price = 7.50

total_cost = bonito_price * bonito_kilograms + scad_price * scad_kilograms + mussels_price * mussels_kilograms

print(f"{total_cost:.2f}")
