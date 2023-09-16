nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
bags = 0.4

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())
extra_nylon = 2
extra_paint = paint_needed * 0.1

money_for_nylon = (nylon_needed + extra_nylon) * nylon_price
money_for_paint = (paint_needed + extra_paint) * paint_price
money_for_thinner = thinner_needed * thinner_price
total_money_for_materials = money_for_nylon + money_for_paint + money_for_thinner + bags
money_for_workers = (total_money_for_materials * 0.3) * hours_needed
total = total_money_for_materials + money_for_workers
print(total)


