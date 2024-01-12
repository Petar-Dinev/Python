budget = int(input())
command = input()

while command != 'End':

    price = int(command)

    if budget < price:
        print("You went in overdraft!")
        break

    budget -= price
    command = input()

else:
    print("You bought everything needed.")
