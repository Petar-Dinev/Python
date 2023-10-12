type_of_ticket = input()
rolls = int(input())
cols = int(input())

seats = cols * rolls
price = 0
if type_of_ticket == 'Premiere':
    price = 12
elif type_of_ticket == 'Normal':
    price = 7.5
elif type_of_ticket == 'Discount':
    price = 5

total = seats * price
print(f"{total:.2f} leva")
