pack_of_pens_price = 5.8
pack_of_markers_price = 7.2
price_of_liter_detergent = 1.2

numbers_packs_of_pens = int(input())
numbers_packs_of_markers = int(input())
litres_of_detergent = int(input())
discount = int(input())

total_price_without_discount = pack_of_pens_price * numbers_packs_of_pens + pack_of_markers_price * numbers_packs_of_markers + price_of_liter_detergent * litres_of_detergent
total_price = total_price_without_discount - total_price_without_discount * discount / 100
print(total_price)

