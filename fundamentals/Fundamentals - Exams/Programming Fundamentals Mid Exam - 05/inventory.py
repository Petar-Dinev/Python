items = input().split(', ')

line = input()

while line != 'Craft!':
    tokens = line.split(' - ')
    command = tokens[0]
    if command == 'Collect':
        item = tokens[1]
        if item not in items:
            items.append(item)
    elif command == 'Drop':
        item = tokens[1]
        if item in items:
            items.remove(item)
    elif command == "Renew":
        item = tokens[1]
        if item in items:
            items.remove(item)
            items.append(item)
    else:
        old_item, new_item = tokens[1].split(':')
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    line = input()

print(', '.join(items))
