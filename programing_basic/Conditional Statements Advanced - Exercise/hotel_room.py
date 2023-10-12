month = input()
nights = int(input())
cost_for_studio = 0
cost_for_apartment = 0

if month == 'May' or month == 'October':
    cost_for_studio = 50 * nights
    cost_for_apartment = 65 * nights
    if 7 < nights <= 14:
        cost_for_studio *= 0.95
    elif nights > 14:
        cost_for_studio *= 0.7
elif month == 'June' or month == 'September':
    cost_for_studio = nights * 75.20
    cost_for_apartment = nights * 68.70
    if nights > 14:
        cost_for_studio *= 0.8
else:
    cost_for_studio = nights * 76
    cost_for_apartment = nights * 77

if nights > 14:
    cost_for_apartment *= 0.9

print(f"Apartment: {cost_for_apartment:.2f} lv.")
print(f"Studio: {cost_for_studio:.2f} lv.")