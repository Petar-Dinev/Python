money = float(input())
current_money = int(money * 100)
coins = 0

while current_money > 0:
    if current_money >= 200:
        coins += 1
        current_money -= 200
    elif current_money >= 100:
        coins += 1
        current_money -= 100
    elif current_money >= 50:
        coins += 1
        current_money -= 50
    elif current_money >= 20:
        coins += 1
        current_money -= 20
    elif current_money >= 10:
        coins += 1
        current_money -= 10
    elif current_money >= 5:
        coins += 1
        current_money -= 5
    elif current_money >= 2:
        coins += 1
        current_money -= 2
    elif current_money == 1:
        coins += 1
        current_money -= 1
print(coins)

