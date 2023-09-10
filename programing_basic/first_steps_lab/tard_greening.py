price_for_one_meter_landscaping = 7.61
percent_discount = 18 / 100
meters_for_landscaping = float(input())
total_without_discount = meters_for_landscaping * price_for_one_meter_landscaping
discount = total_without_discount * percent_discount
total = total_without_discount - discount
print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")