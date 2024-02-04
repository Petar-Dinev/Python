gifts_need_to_buy = input().split()
next_line = input()

while next_line != 'No Money':
    tokens = next_line.split()
    command = tokens[0]
    current_gift = tokens[1]

    if command == 'OutOfStock':
        while current_gift in gifts_need_to_buy:
            index_to_insert = gifts_need_to_buy.index(current_gift)
            gifts_need_to_buy.remove(current_gift)
            gifts_need_to_buy.insert(index_to_insert, 'None')
    elif command == 'Required':
        index = int(tokens[2])
        if 0 <= index < len(gifts_need_to_buy):
            gifts_need_to_buy.pop(index)
            gifts_need_to_buy.insert(index, current_gift)
    elif command == 'JustInCase':
        gifts_need_to_buy[-1] = current_gift

    next_line = input()

for gift in gifts_need_to_buy:
    if gift != "None":
        print(gift, end=' ')
